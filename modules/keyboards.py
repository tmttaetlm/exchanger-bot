from telebot import types

def keyboard(type, params = {}):
    if type == 'mainmenu':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
        keyboard.add(types.KeyboardButton('Курсы валют в моем городе'))
        keyboard.add(types.KeyboardButton('Обменные пункты по валюте'))
        keyboard.add(types.KeyboardButton('Калькулятор конвертации валют'))
        keyboard.add(types.KeyboardButton('Сменить город'))
    if type == 'cities':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.row(types.InlineKeyboardButton('Алматы', callback_data = 'city_almaty'),
                    types.InlineKeyboardButton('Астана', callback_data = 'city_astana'),
                    types.InlineKeyboardButton('Шымкент', callback_data = 'city_shymkent'))
        keyboard.row(types.InlineKeyboardButton('Актау', callback_data = 'city_aktau'),
                    types.InlineKeyboardButton('Актобе', callback_data = 'city_aktobe'),
                    types.InlineKeyboardButton('Атырау', callback_data = 'city_atyrau'))
        keyboard.row(types.InlineKeyboardButton('Жезказган', callback_data = 'city_zhezkazgan'),
                    types.InlineKeyboardButton('Караганда', callback_data = 'city_karaganda'),
                    types.InlineKeyboardButton('Кокшетау', callback_data = 'city_kokshetau'))
        keyboard.row(types.InlineKeyboardButton('Костанай', callback_data = 'city_kostanay'),
                    types.InlineKeyboardButton('Кызылорда', callback_data = 'city_kyzylorda'),
                    types.InlineKeyboardButton('Павлодар', callback_data = 'city_pavlodar'))
        keyboard.row(types.InlineKeyboardButton('Петропавловск', callback_data = 'city_petropavlovsk'),
                    types.InlineKeyboardButton('Семей', callback_data = 'city_semey'),
                    types.InlineKeyboardButton('Талдыкорган', callback_data = 'city_taldykorgan'))
        keyboard.row(types.InlineKeyboardButton('Тараз', callback_data = 'city_taraz'),
                    types.InlineKeyboardButton('Темиртау', callback_data = 'city_temirtau'),
                    types.InlineKeyboardButton('Туркестан', callback_data = 'city_turkistan'))
        keyboard.row(types.InlineKeyboardButton('Уральск', callback_data = 'city_uralsk'),
                    types.InlineKeyboardButton('Усть-Каменогорск', callback_data = 'city_ust-kamenogorsk'),
                    types.InlineKeyboardButton('Экибастуз', callback_data = 'city_ekibastuz'))
    if type == 'currencies':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.row(types.InlineKeyboardButton('KZT', callback_data = 'currency_kzt'),
                    types.InlineKeyboardButton('USD', callback_data = 'currency_usd'),
                    types.InlineKeyboardButton('EUR', callback_data = 'currency_eur'),
                    types.InlineKeyboardButton('RUB', callback_data = 'currency_rub'))
    if type == 'actions':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.row(types.InlineKeyboardButton('Хочу обменять', callback_data = 'action_from'))
        keyboard.row(types.InlineKeyboardButton('Хочу получить', callback_data = 'action_to'))
    return keyboard