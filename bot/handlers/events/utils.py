from aiogram import types, Bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import os


from ..button import *


async def start(msg: types.Message):
    bot = Bot(token=os.getenv("TOKEN"))
    await msg.answer("Здравствуйте, вас приветсвует бот Акито для заказов еды из Япономании", reply_markup=reply_key.kb_menu)
    await bot.send_sticker(chat_id=msg.from_user.id,
                           sticker="CAACAgIAAxkBAAEHWhljyjqS5fuAdW0BWjaX4omEEW8oCAAChhIAApOFuEh_Z5OyWMQEVi0E")
    await msg.delete()

async def register(msg: types.Message):
    #check database
    
    await msg.answer('Выберите пункт:', reply_markup= reply_key.kb_register)
    

async def cancel_register(msg: types.Message):
    await msg.answer('Возвращаю', reply_markup= reply_key.kb_menu)

async def order(msg: types.Message):
    await msg.answer('Находи курьера на астеройде...', reply_markup= reply_key.kb_order)

async def find_orders(msg: types.Message):
    await msg.answer('Находим заказы')

async def profile(msg: types.Message):
    await msg.answer('Находим данные с комет...', reply_markup= reply_key.kb_profile)

async def find_points(msg: types.Message):
    await msg.answer('Выводим кол-во поинтов...')
    
