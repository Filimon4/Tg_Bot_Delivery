from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


kb_menu = ReplyKeyboardMarkup(
    keyboard = [ 
        [
            KeyboardButton(text= '✍регистрация'),
            KeyboardButton(text= '🤖заказ') 
        ]
], resize_keyboard=True)