import telebot
from modules.mongo import get_collection
from modules.functions import currency_rate_msg

bot = telebot.TeleBot('5299933627:AAFadtni2QPlSxeikWyTYNN-DukFGkm_KY0')

collection = get_collection('users')
users = collection.find()
for user in users:
    if not user['subscription']: continue
    bot.send_message(user['id'], currency_rate_msg(user['city']), parse_mode='HTML')