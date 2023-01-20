from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


kb_menu = ReplyKeyboardMarkup(
    keyboard = [ 
        [
            KeyboardButton(text= '✍регистрация'),
            KeyboardButton(text= '🤖заказ') 
        ],
        [
            KeyboardButton(text= '🤝напишите отзыв')
        ]
], resize_keyboard=True)

kb_register = ReplyKeyboardMarkup(
    keyboard = [ 
        [
            KeyboardButton(text= 'Пройти регистрацию'),
            KeyboardButton(text= 'Назад') 
        ]
    ], resize_keyboard=True)