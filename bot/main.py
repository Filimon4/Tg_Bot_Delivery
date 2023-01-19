from aiogram import Bot, Dispatcher, executor, types
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from .database import *
from .handlers import *

storage = MemoryStorage()

async def create_logic(dp: Dispatcher):
    start_database(dp)
    set_handlers(dp)

def start_bot():
    bot = Bot(token=os.getenv("TOKEN"))
    dp = Dispatcher(bot, storage= storage)
    executor.start_polling(dp, skip_updates=True, on_startup=create_logic)