from aiogram import types,Dispatcher

from .utils import *

def set_events(dp: Dispatcher):
    dp.register_message_handler(start, commands = "start")