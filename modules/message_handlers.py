from modules.keyboards import keyboard
from modules.mongo import get_collection
from modules.functions import currency_rate_msg, converted_currency_msg

def message_handler(bot, message):
    collection = get_collection('users')
    user = collection.find_one({'id': message.from_user.id})

    if message.text == 'Курсы валют в моем городе':
        city = user['city']
        bot.send_message(message.from_user.id, currency_rate_msg(city), parse_mode='HTML')

    if message.text == 'Обменные пункты по валюте':
        res = bot.send_message(message.from_user.id, 'Выберите валюту', reply_markup=keyboard('currencies'), parse_mode='HTML')
        collection.update_one({'id': message.from_user.id}, {'$set': {'msg_id': res.id }})

    if message.text == 'Калькулятор конвертации валют':
        res = bot.send_message(message.from_user.id, 'Выберите действие', reply_markup=keyboard('actions'), parse_mode='HTML')
        collection.update_one({'id': message.from_user.id}, {'$set': {'msg_id': res.id }})

    if message.text == 'Сменить город':
        city = user['city']
        res = bot.send_message(message.from_user.id, f'Ваш текущий город {city}.\nВыберите другой город', reply_markup=keyboard('cities'), parse_mode='HTML')
        collection.update_one({'id': message.from_user.id}, {'$set': {'msg_id': res.id }})

    if user['action'] is not None and user['currency_from'] is not None and user['currency_to'] is not None:
        res = bot.send_message(message.from_user.id, converted_currency_msg(), parse_mode='HTML')
        collection.update_one({'id': message.from_user.id}, {'$set': {'action': None, 'currency_from': None, 'currency_to': None}})
