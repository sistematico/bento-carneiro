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
    context.bot.deleteMessage(chat_id=update.message.chat_id, message_id=update.message.message_id)
    #update.message.reply_text('Estou reiniciando...')
    context.bot.send_message(update.message.chat_id, 'Estou reiniciando...')
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
    update.message.reply_markdown_v2(fr'Olá {user.mention_markdown_v2()}\!', reply_markup=ForceReply(selective=True),)

@send_action(ChatAction.TYPING)
def status(update: Update, context: CallbackContext) -> None:
    #member = context.bot.get_chat_member(message.chat.id)
    # member = context.bot.get_chat_member(update.message.chat_id, context.bot.user_id)
    # for x in member:
    for x in context.bot:
        arg = ''.join(x)
        context.bot.send_message(update.message.chat_id, str(arg))
        #context.bot.send_message(update.message.chat_id, str(vars(x)))
        #print(x)
        #print vars(x)
        #print( vars(x) )

@send_action(ChatAction.TYPING)
def hello(update: Update, context: CallbackContext) -> None:
    # update.message.sendMessage(f'Hello {update.effective_user.first_name}')
    #context.bot.send_message(f'Hello {update.effective_user.first_name}')
    context.bot.send_message(update.message.chat_id, f'Hello {update.effective_user.first_name}')

def delete(update: Update, context: CallbackContext) -> None:
    messageId = update.message.message_id
    chatId = update.message.chat.id
    
    if any(x in update.message.text for x in blacklist):
        context.bot.delete_message(chat_id=chatId, message_id=messageId)
        #context.bot.delete_message(chat_id=update.effective_message.chat_id, message_id=update.effective_message.message_id)

updater = Updater(TOKEN)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('status', status))

updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, delete))
updater.dispatcher.add_handler(CommandHandler('r', restart, filters=Filters.user(username='@sistematico')))

updater.start_polling()
updater.idle()