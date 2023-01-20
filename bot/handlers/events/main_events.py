from aiogram import types,Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


from .utils import *

def set_events(dp: Dispatcher):
    dp.register_message_handler(start, commands = "start")
    dp.register_message_handler(register, text = "✍регистрация")
    dp.register_message_handler(order, text = "🤖заказ")
    dp.register_message_handler(profile, text = "👤Профиль")
    dp.register_message_handler(find_points, text = 'Посмотреть кол-во баллов')
    dp.register_message_handler(make_order, text = "Сделать Заказ")
    dp.register_message_handler(find_orders, text = "Посмотреть все заказы")
    dp.register_message_handler(cancel_register, text= 'Назад')
