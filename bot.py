import telebot
from tabulate import tabulate
from modules.keyboards import keyboard
from modules.message_handlers import message_handler
from modules.callback_handlers import callback_handler
from modules.parser import get_currency_rate
from modules.mongo import get_collection

bot = telebot.TeleBot('5299933627:AAFadtni2QPlSxeikWyTYNN-DukFGkm_KY0')

@bot.message_handler(commands=['start'])
def start_message(message):
    collection = get_collection('users')
    cd = collection.count_documents({ 'id':  message.from_user.id })
    if cd == 0:
        data = {
            'id':  message.from_user.id,
            'username': message.from_user.username if message.from_user.username is not None else '',
            'first_name': message.from_user.first_name if message.from_user.first_name is not None else '',
            'last_name': message.from_user.last_name if message.from_user.last_name is not None else '',
        }
        collection.insert_one(data)
        bot.send_message(message.chat.id, "Выберите город", reply_markup=keyboard('cities'))
    else:
        for el in collection.find_one({'id': message.from_user.id}):
            city = el.city
        currency = get_currency_rate(city)
        cols = ['Валюта', 'Покупка', 'Продажа']
        msg = tabulate(currency, headers=cols, stralign='right', colalign=('left',))
        bot.send_message(message.from_user.id, '<pre>'+msg+'</pre>', parse_mode='HTML')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    message_handler(bot, message)

@bot.callback_query_handler(func=lambda call: True)
def user_callbacks(call):
    callback_handler(bot, call)

bot.infinity_polling()