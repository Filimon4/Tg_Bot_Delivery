from aiogram import Bot, Dispatcher, executor, types
import os

from .database import *
from .handlers import *

async def create_logic(dp: Dispatcher):
    start_database(dp)
    set_handlers(dp)

def start_bot():
    bot = Bot(token=os.getenv("TOKEN"))
    dp = Dispatcher(bot)
    executor.start_polling(dp, skip_updates=True, on_startup=create_logic)