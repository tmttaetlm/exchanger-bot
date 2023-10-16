from modules.keyboards import keyboard
from modules.mongo import get_collection
from modules.functions import currency_rate_msg, converted_currency_msg

def message_handler(bot, message):
    collection = get_collection('users')
    user = collection.find_one({'id': message.from_user.id})

    if message.text == 'Р':
        bot.send_message(message.from_user.id, 'Главное меню', reply_markup=keyboard('mainmenu', {'subscription': user['subscription']}), parse_mode='HTML')

    if message.text == 'Курсы валют в моем городе':
        bot.send_message(message.from_user.id, currency_rate_msg(user['city']), parse_mode='HTML')

    if message.text == 'Обменные пункты по валюте':
        res = bot.send_message(message.from_user.id, 'Выберите валюту', reply_markup=keyboard('currencies', {'need_kzt': False}), parse_mode='HTML')
        collection.update_one({'id': message.from_user.id}, {'$set': {'msg_id': res.id, 'mode': None, 'step': None }})

    if message.text == 'Калькулятор конвертации валют':
        res = bot.send_message(message.from_user.id, 'Выберите действие', reply_markup=keyboard('actions'), parse_mode='HTML')
        collection.update_one({'id': message.from_user.id}, {'$set': {'msg_id': res.id, 'mode': 'convert', 'step': 1, 'action': None, 'currency_from': None, 'currency_to': None }})

    if message.text == 'Сменить город':
        res = bot.send_message(message.from_user.id, 'Ваш текущий город '+user['city']+'.\nВыберите другой город', reply_markup=keyboard('cities'), parse_mode='HTML')
        collection.update_one({'id': message.from_user.id}, {'$set': {'msg_id': res.id }})

    if message.text == 'Включить мониторинг курса':
        res = bot.send_message(message.from_user.id, 
                               'Мониторинг курсов включен. Вы будете получать уведомление с курсами валют два раза в день - утром в 10.00 и днем в 15.00', 
                               reply_markup=keyboard('mainmenu', {'subscription': True}), 
                               parse_mode='HTML')
        collection.update_one({'id': message.from_user.id}, {'$set': {'subscription': True }})
    if message.text == 'Отключить мониторинг курса':
        res = bot.send_message(message.from_user.id, 
                               'Мониторинг курсов отключен', 
                               reply_markup=keyboard('mainmenu', {'subscription': False}),
                               parse_mode='HTML')
        collection.update_one({'id': message.from_user.id}, {'$set': {'subscription': False }})

    if user['mode'] == 'convert' and user['step'] == 4:
        res = bot.send_message(message.from_user.id, converted_currency_msg(user['city'], user['action'], user['currency_from'], user['currency_to'], message.text), parse_mode='HTML')
        collection.update_one({'id': message.from_user.id}, {'$set': {'action': None, 'currency_from': None, 'currency_to': None, 'mode': None, 'step': None}})
