import telebot
from modules.mongo import get_collection
from modules.functions import currency_rate_msg

bot = telebot.TeleBot('5822916674:AAGf_tMq-GAks2YoOFcbIMkzYNeU8tKK9Zk')

collection = get_collection('users')
users = collection.find()
for user in users:
    if not user['subscription']: continue
    bot.send_message(user['id'], currency_rate_msg(user['city']), parse_mode='HTML')