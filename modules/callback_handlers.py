from modules.mongo import get_collection
from modules.keyboards import keyboard
from modules.functions import currency_rate_msg, exchenger_list_msg

def callback_handler(bot, callback):
    collection = get_collection('users')
    user = collection.find_one({'id': callback.from_user.id})

    if callback.data.startswith('city_'):
        city = callback.data[callback.data.index('_')+1:len(callback.data)]
        try: bot.delete_message(callback.from_user.id, user['msg_id'])
        except: pass
        collection.update_one({'id': callback.from_user.id}, {'$set': {'city': city }})
        bot.send_message(callback.from_user.id, currency_rate_msg(city), reply_markup=keyboard('mainmenu'), parse_mode='HTML')
        
    if callback.data.startswith('currency_'):
        currency = callback.data[callback.data.index('_')+1:len(callback.data)]
        try: bot.delete_message(callback.from_user.id, user['msg_id'])
        except: pass
        if user['mode'] == 'convert':
            if user['step'] == 2:
                collection.update_one({'id': callback.from_user.id}, {'$set': {'currency_from': currency, 'mode': 'convert', 'step': 3 }})
                res = bot.send_message(callback.from_user.id, 'Выберите вторую валюту', reply_markup=keyboard('currencies'), parse_mode='HTML')
            if user['step'] == 3:
                collection.update_one({'id': callback.from_user.id}, {'$set': {'currency_to': currency, 'mode': 'convert', 'step': 4 }})
                res = bot.send_message(callback.from_user.id, 'Введите сумму', parse_mode='HTML')
            collection.update_one({'id': callback.from_user.id}, {'$set': {'msg_id': res.id }})
        else:
            bot.send_message(callback.from_user.id, exchenger_list_msg(user['city'], currency), parse_mode='HTML')

    if callback.data.startswith('action_'):
        action = callback.data[callback.data.index('_')+1:len(callback.data)]
        try: bot.delete_message(callback.from_user.id, user['msg_id'])
        except: pass
        res = bot.send_message(callback.from_user.id, 'Выберите первую валюту', reply_markup=keyboard('currencies'), parse_mode='HTML')
        collection.update_one({'id': callback.from_user.id}, {'$set': {'msg_id': res.id, 'action': action, 'mode': 'convert', 'step': 2 }})