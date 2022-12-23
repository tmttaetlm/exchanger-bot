from datetime import datetime
from tabulate import tabulate
from modules.parser import get_currency_rate

def currency_rate_msg(city):
    currency = get_currency_rate(city)
    msg = f'Курс валют в городе {city} на {datetime.now().strftime("%d.%m.%Y %H:%M:%S")}\n'
    cols = ['Валюта', 'Покупка', 'Продажа']
    msg += tabulate(currency, headers=cols, stralign='right', colalign=('left',))
    return '<code>'+msg+'</code>'