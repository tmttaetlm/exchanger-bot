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