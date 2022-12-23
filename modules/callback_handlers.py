from modules.mongo import get_collection
from modules.keyboards import keyboard
from modules.functions import currency_rate_msg

def callback_handler(bot, callback):
    if callback.data.startswith('city_'):
        city = callback.data[callback.data.index('_')+1:len(callback.data)]
        collection = get_collection('users')
        msg_id = collection.find_one({'id': callback.from_user.id})['msg_id']
        try: bot.delete_message(callback.from_user.id, msg_id)
        except: pass
        collection.update_one({'id': callback.from_user.id}, {'$set': {'city': city }})

        bot.send_message(callback.from_user.id, 
                        currency_rate_msg(city), 
                        reply_markup=keyboard('mainmenu'), 
                        parse_mode='HTML')
