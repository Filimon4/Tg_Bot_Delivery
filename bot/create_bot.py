from aiogram import Bot,types,Dispatcher
import os

bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher(bot)