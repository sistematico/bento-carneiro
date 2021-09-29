import os
import sys
from threading import Thread
from telegram import Update, ChatAction, ForceReply
from telegram.ext import Updater, MessageHandler, CommandHandler, CallbackContext, Filters
from functools import wraps
from config.config import TOKEN
from config.blacklist import blacklist

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
def status(update: Update, context: CallbackContext) -> None:
    member = context.bot.get_chat_member(message.chat.id)
    for x in member:
        print(x)

@send_action(ChatAction.TYPING)
def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

    #print vars(foo)

@send_action(ChatAction.TYPING)
def delete(update: Update, context: CallbackContext) -> None:
    #update.message.reply_text(f'Hello {update.effective_user.first_name}')
    #update.delete_message(chat_id=message.chat_id, message_id=message.message_id, *args, **kwargs)
    #must_delete = update.message.reply_text("Please delete: ")
    #context.bot.deleteMessage(message_id = must_delete.message_id, chat_id = update.message.chat_id)
    if any(x in update.message.text for x in blacklist):
        context.bot.deleteMessage(chat_id=update.message.chat_id, message_id=update.message.message_id)

updater = Updater(TOKEN)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, delete))

updater.dispatcher.add_handler(CommandHandler('r', restart, filters=Filters.user(username='@sistematico')))

updater.start_polling()
updater.idle()