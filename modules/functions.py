from datetime import datetime
from tabulate import tabulate
from modules.parser import get_currency_rate, get_exchanger_list, get_converted_currency

def currency_rate_msg(city):
    currency = get_currency_rate(city)
    msg = f'Курс валют в городе {city} на {datetime.now().strftime("%d.%m.%Y %H:%M:%S")}\n\n'
    cols = ['Валюта', 'Покупка', 'Продажа']
    msg += tabulate(currency, headers=cols, stralign='right', colalign=('left',))
    return '<pre>'+msg+'</pre>'

def exchenger_list_msg(city, currency):
    exchanger = get_exchanger_list(city, currency)
    msg = f'Курс {currency} в городе {city} на {datetime.now().strftime("%d.%m.%Y %H:%M:%S")}\n\n'
    cols = ['', 'Покупка', 'Продажа']
    msg += tabulate(exchanger, headers=cols, stralign='right', colalign=('left',), maxcolwidths=[13, 9, 9])
    return '<pre>'+msg+'</pre>'

def converted_currency_msg(city, action, currency_from, currency_to, count):
    converter = get_converted_currency(city, action, currency_from, currency_to, count)
    cols = ['Обменник', 'Курс', 'Сумма']
    msg = tabulate(converter, headers=cols, stralign='right', colalign=('left',), maxcolwidths=[13, 9, 9])
    return '<pre>'+msg+'</pre>'