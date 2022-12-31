import requests
from bs4 import BeautifulSoup as bs

def get_currency_rate(city='kostanay'):
    r = requests.get(f'https://ifin.kz/?city={city}')
    html = bs(r.content, 'html.parser')
    main = html.find(id='page-main')
    lst = main.find(class_='col-lg-6').find_all(class_='row-flex')
    result = []
    for i in range(len(lst)):
        tmp = []
        currency = main.find(class_='col-flex col-lg-3').find_all(class_="text-detail")
        tmp.append(currency[i].text.lstrip('1 '))
        buy = lst[i].find(class_='col-lg-12').contents[1].find(class_='currency-rate-big')
        tmp.append(buy.text.strip().replace(' ', '').replace('\n', ': '))
        sell = lst[i].find(class_='col-lg-12').contents[3].find(class_='currency-rate-big')
        tmp.append(sell.text.strip().replace(' ', '').replace('\n', ': '))
        result.append(tmp)
    return result

def get_exchanger_list(city='kostanay', currency='USD'):
    r = requests.get(f'https://ifin.kz/exchange/{city}/{currency.upper()}')
    html = bs(r.content, 'html.parser')
    main = html.find(class_='tbl-hovered')
    lst = main.find_all(class_='tbl-row')
    result = []
    for el in lst:
        tmp = []
        exchanger = el.contents[3].find('a').text.strip().replace('\n', ': ')
        sell_price = el.contents[5].find('span').text.strip().replace('\n', ': ')
        buy_price = el.contents[7].find('span').text.strip().replace('\n', ': ')
        tmp.append(exchanger)
        tmp.append(sell_price)
        tmp.append(buy_price)
        result.append(tmp)
    return result

def get_converted_currency(city='kostanay', action='from', currency_from='USD', currency_to='KZT', count='1000'):
    link = f'https://ifin.kz/exchange/search?city={city}&ExchangeForm[method]={action}&ExchangeForm[count]={count}&ExchangeForm[currencyFrom]={currency_from.upper()}&ExchangeForm[currencyTo]={currency_to.upper()}'
    print(link)
    r = requests.get(link)
    html = bs(r.content, 'html.parser')
    main = html.find(id='p0')
    lst = main.find_all(class_='tbl-row')
    result = []
    for el in lst:
        tmp = []
        exchanger = el.contents[3].find('a').text.strip().replace('\n', ': ')
        price = el.contents[5].find('span').text.strip().replace('\n', ': ')
        summary = el.contents[7].find('b').text.strip().replace('\n', ': ')
        tmp.append(exchanger)
        tmp.append(price)
        tmp.append(summary)
        result.append(tmp)
    return result
