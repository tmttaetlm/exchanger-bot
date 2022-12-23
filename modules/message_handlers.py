from modules.keyboards import keyboard
from modules.mongo import get_collection
from modules.functions import currency_rate_msg

def message_handler(bot, message):
    if message.text == 'Курсы валют в моем городе':
        collection = get_collection('users')
        city = collection.find_one({'id': message.from_user.id})['city']
        bot.send_message(message.from_user.id,
                        currency_rate_msg(city),
                        reply_markup=keyboard('mainmenu'),
                        parse_mode='HTML')

    if message.text == 'Сменить город':
        collection = get_collection('users')
        city = collection.find_one({'id': message.from_user.id})['city']
        res = bot.send_message(message.from_user.id, 
                        f'Ваш текущий город {city}.\nВыберите другой город', 
                        reply_markup=keyboard('cities'), 
                        parse_mode='HTML')
        collection.update_one({'id': message.from_user.id}, {'$set': {'msg_id': res.id }})
