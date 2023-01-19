from aiogram import types,Dispatcher

from .utils import *

def set_events(dp: Dispatcher):
    dp.register_message_handler(start, commands = "start")
    dp.register_message_handler(register, commands = "✍регистрация")
    dp.register_message_handler(order, commands = "🤖 заказ")