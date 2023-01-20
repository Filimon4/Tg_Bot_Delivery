from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from .create_bot import *
import os

from .database import *
from .handlers import *

storage = MemoryStorage()

async def create_logic(dp: Dispatcher):
    start_database(dp)
    set_handlers(dp)

def start_bot():
    executor.start_polling(dp, skip_updates=True, on_startup=create_logic)