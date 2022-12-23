from tabulate import tabulate
from modules.keyboards import keyboard
from modules.parser import get_currency_rate
from modules.mongo import get_collection

def message_handler(bot, message):
    if message.text == 'Курсы валют в моем городе':
        collection = get_collection('users')
        for el in collection.find_one({'id': message.from_user.id}):
            city = el.city
        currency = get_currency_rate(city)
        cols = ['Валюта', 'Покупка', 'Продажа']
        msg = tabulate(currency, headers=cols, stralign='right', colalign=('left',))
        bot.send_message(message.from_user.id, '<pre>'+msg+'</pre>', parse_mode='HTML')
    