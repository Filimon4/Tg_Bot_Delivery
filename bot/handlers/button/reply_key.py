from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


kb_menu = ReplyKeyboardMarkup(
    keyboard = [ 
        [
            KeyboardButton(text= '✍регистрация'),
            KeyboardButton(text= '🤖заказ') 
        ]
], resize_keyboard=True)
Register = ReplyKeyboardMarkup(
    keyboard = [ 
        [
            KeyboardButton(text= 'Пройти регистрацию'),
            KeyboardButton(text= 'Назад') 
        ]
    ], resize_keyboard=True)