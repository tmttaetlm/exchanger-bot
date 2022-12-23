from datetime import datetime
from tabulate import tabulate
from modules.keyboards import keyboard
from modules.parser import get_currency_rate
from modules.mongo import get_collection

def callback_handler(bot, callback):
    if callback.data.startswith('city_'):
        city = callback.data[callback.data.index('_')+1:len(callback.data)]
        collection = get_collection('users')

        msg_id = collection.find_one({'id': callback.from_user.id})['msg_id']
        try: bot.delete_message(callback.from_user.id, msg_id)
        except: pass
        collection.update_one({'id': callback.from_user.id}, {'$set': {'city': city }})

        currency = get_currency_rate(city)
        msg = f'Курс валют в городе {city} на {datetime.now().strftime("%d.%m.%Y %H:%M:%S")}'
        cols = ['Валюта', 'Покупка', 'Продажа']
        msg += tabulate(currency, headers=cols, stralign='right', colalign=('left',))
        bot.send_message(callback.from_user.id, '<pre>'+msg+'</pre>', parse_mode='HTML')
    