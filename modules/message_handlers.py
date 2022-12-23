from datetime import datetime
from tabulate import tabulate
from modules.keyboards import keyboard
from modules.parser import get_currency_rate
from modules.mongo import get_collection

def message_handler(bot, message):
    if message.text == 'Курсы валют в моем городе':
        collection = get_collection('users')
        city = collection.find_one({'id': message.from_user.id})['city']
        currency = get_currency_rate(city)
        msg = f'Курс валют в городе {city} на {datetime.now.strftime("%d.%m.%Y %H:%M:%S")}'
        cols = ['Валюта', 'Покупка', 'Продажа']
        msg += tabulate(currency, headers=cols, stralign='right', colalign=('left',))
        bot.send_message(message.from_user.id, '<pre>'+msg+'</pre>', parse_mode='HTML')

    if message.text == 'Сменить город':
        collection = get_collection('users')
        city = collection.find_one({'id': message.from_user.id})['city']
        bot.send_message(message.from_user.id, 
                        f'Ваш текущий город {city}.\nВыберите другой город', 
                        reply_markup=keyboard('cities'), 
                        parse_mode='HTML')
