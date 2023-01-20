from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


kb_menu = ReplyKeyboardMarkup(
    keyboard = [ 
        [
            KeyboardButton(text= '✍регистрация'),
            KeyboardButton(text= '🤖заказ') 
        ],
        [
            KeyboardButton(text= '🤝напишите отзыв')
        ],
        [
            KeyboardButton(text= '👤Профиль')
        ]
], resize_keyboard=True)

kb_register = ReplyKeyboardMarkup(
    keyboard = [ 
        [
            KeyboardButton(text= 'Пройти регистрацию'),
            KeyboardButton(text= 'Назад') 
        ]
    ], resize_keyboard=True)

kb_order = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text= "Сделать Заказ"),
            KeyboardButton(text= "Посмотреть все заказы"),
        ],
        [
            KeyboardButton(text= "Назад"),
        ]
    ], resize_keyboard=True)