import os
import sys
from threading import Thread
from telegram import Update, ChatAction
from telegram.ext import Updater, MessageHandler, CommandHandler, CallbackContext
from functools import wraps
from config import TOKEN

def stop_and_restart():
    """Gracefully stop the Updater and replace the current process with a new one"""
    updater.stop()
    os.execl(sys.executable, sys.executable, *sys.argv)

def restart(update, context):
    update.message.reply_text('Estou reiniciando...')
    Thread(target=stop_and_restart).start()

def send_action(action):
    """Sends `action` while processing func command."""

    def decorator(func):
        @wraps(func)
        def command_func(update, context, *args, **kwargs):
            context.bot.send_chat_action(chat_id=update.effective_message.chat_id, action=action)
            return func(update, context,  *args, **kwargs)
        return command_func
    
    return decorator

def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )

@send_action(ChatAction.TYPING)
def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

@send_action(ChatAction.TYPING)
def delete(update: Update, context: CallbackContext) -> None:
    #update.message.reply_text(f'Hello {update.effective_user.first_name}')
    #update.delete_message(chat_id=message.chat_id, message_id=message.message_id, *args, **kwargs)
    update.delete_message(chat_id=message.chat_id, message_id=message.message_id)

updater = Updater(TOKEN)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, delete))

updater.dispatcher.add_handler(CommandHandler('r', restart, filters=Filters.user(username='@sistematico')))

updater.start_polling()
updater.idle()