from aiogram import Bot, Dispatcher, executor, types
import os

async def create_logic(dp: Dispatcher):
    pass

def start_bot():
    bot = Bot(token=os.getenv("TOKEN"))
    dp = Dispatcher(bot)
    executor.start_polling(dp, skip_updates=True, on_startup=create_logic)