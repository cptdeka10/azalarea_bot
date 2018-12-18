import os
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import telegram.ext

from datetime import datetime, timedelta
from pytz import timezone
import pytz


# add responses
def start(bot, update):
    update.effective_message.reply_text("Um... Let's do our best......today.", quote=False)
    
def caps(bot, update,args):
    text_caps = ' '.join(args).upper()
    update.effective_message.reply_text(text_caps)

def bio(bot, update):
    update.effective_message.reply_text("Name       : 	望月杏奈 (Mochizuki Anna) \nBirthday   : 	May 31st \nBlood type: 	AB \nHobbies    : 	Online games \nSkill      : 	Typing \nLikes      : 	Cute things", quote=False)

def ping (bot, update):
    update.effective_message.reply_text("Um... I'm...OK.", quote=False)

def time (bot, update,args):
    args_caps = ' '.join(args).upper()
    target = timezone(args_caps)
    target_tz = target.localize(telegram.Message.date)
    update.effective_message.reply_text("The date and time in ", args, " is ", target_tz)

# add handlers
start_handler = CommandHandler('start', start)
caps_handler = CommandHandler('caps', caps, pass_args=True)
bio_handler = CommandHandler('bio', bio)
ping_handler = CommandHandler('ping', ping)
time_handler = CommandHandler('time', time, pass_args=True)

if __name__ == "__main__":
    NAME = "AnnaMochizukiBot"
    TOKEN = os.environ['TOKEN']
    
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
    logger = logging.getLogger(__name__)
    
    PORT = os.environ.get('PORT')
    updater = Updater(TOKEN)
    
    dp = updater.dispatcher
    dp.add_handler(start_handler)
    dp.add_handler(caps_handler)
    dp.add_handler(bio_handler)
    dp.add_handler(ping_handler)
    dp.add_handler(time_handler)
    
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.set_webhook("https://{}.herokuapp.com/{}".format(NAME, TOKEN))
updater.idle()
