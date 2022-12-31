from modules.keyboards import keyboard
from modules.mongo import get_collection
from modules.functions import currency_rate_msg, converted_currency_msg

def message_handler(bot, message):
    collection = get_collection('users')
    user = collection.find_one({'id': message.from_user.id})

    if message.text == 'Курсы валют в моем городе':
        bot.send_message(message.from_user.id, currency_rate_msg(user['city']), parse_mode='HTML')

    if message.text == 'Обменные пункты по валюте':
        res = bot.send_message(message.from_user.id, 'Выберите валюту', reply_markup=keyboard('currencies'), parse_mode='HTML')
        collection.update_one({'id': message.from_user.id}, {'$set': {'msg_id': res.id }})

    if message.text == 'Калькулятор конвертации валют':
        res = bot.send_message(message.from_user.id, 'Выберите действие', reply_markup=keyboard('actions'), parse_mode='HTML')
        collection.update_one({'id': message.from_user.id}, {'$set': {'msg_id': res.id, 'mode': 'convert', 'step': 1 }})

    if message.text == 'Сменить город':
        res = bot.send_message(message.from_user.id, 'Ваш текущий город '+user['city']+'.\nВыберите другой город', reply_markup=keyboard('cities'), parse_mode='HTML')
        collection.update_one({'id': message.from_user.id}, {'$set': {'msg_id': res.id }})

    if user['mode'] == 'convert' and user['step'] == 4:
        res = bot.send_message(message.from_user.id, converted_currency_msg(user['city'], user['action'], user['currency_from'], user['currency_to'], message.text), parse_mode='HTML')
        collection.update_one({'id': message.from_user.id}, {'$set': {'action': None, 'currency_from': None, 'currency_to': None, 'mode': None, 'step': None}})
