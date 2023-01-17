from datetime import datetime
from tabulate import tabulate
from modules.mongo import get_collection
from modules.parser import get_currency_rate, get_exchanger_list, get_converted_currency

def currency_rate_msg(city):
    currency = get_currency_rate(city)
    collection = get_collection('cities')
    city_name = collection.find_one({'key': city})['name']
    msg = f'Курс валют в городе {city_name} на {datetime.now().strftime("%d.%m.%Y %H:%M:%S")}\n\n'
    cols = ['Валюта', 'Покупка', 'Продажа']
    msg += tabulate(currency, headers=cols, stralign='right', colalign=('left',))
    return '<pre>'+msg+'</pre>'

def exchenger_list_msg(city, currency):
    exchanger = get_exchanger_list(city, currency)
    collection = get_collection('cities')
    city_name = collection.find_one({'key': city})['name']
    msg = f'Курс {currency.upper()} в городе {city_name} на {datetime.now().strftime("%d.%m.%Y %H:%M:%S")}\n\n'
    cols = ['', 'Покупка', 'Продажа']
    msg += tabulate(exchanger, headers=cols, stralign='right', colalign=('left',), maxcolwidths=[13, 9, 9])
    return '<pre>'+msg+'</pre>'

def converted_currency_msg(city, action, currency_from, currency_to, count):
    converter = get_converted_currency(city, action, currency_from, currency_to, count)
    cols = ['Обменник', 'Курс', 'Сумма']
    msg = tabulate(converter, headers=cols, stralign='right', colalign=('left',), maxcolwidths=[13, 6, 12])
    return '<pre>'+msg+'</pre>'