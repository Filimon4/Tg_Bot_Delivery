from aiogram import types, Bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import os

from ..button import *

async def start(msg: types.Message):
    await msg.answer("Здравствуйте, вас приветсвует бот Акито для заказов еды из Япономании", reply_markup=reply_key.kb_menu)
    await msg.send_sticker(chat_id=msg.from_user.id,
                           sticker=r"CAACAgIAAxkBAAEHWhljyjqS5fuAdW0BWjaX4omEEW8oCAAChhIAApOFuEh_Z5OyWMQEVi0E")
    await msg.delete()

async def register(msg: types.Message):
    #check database
    
    await msg.answer('Ищю межпланетного диспечера...', reply_markup= reply_key.kb_register)
    # await Bot(os.getenv("TOKEN")).send_sticker(chat_id=msg.from_user.id,
    #                        sticker=r"CAACAgIAAxkBAAED7aNiCmNgcLCdHjYZIU2Yf9sLNxTiEAACVhQAAhzIoEuxFOaAT2TuaSME")

async def cancel_register(msg: types.Message):
    await msg.answer('Возвращаю', reply_markup= reply_key.kb_menu)

async def order(msg: types.Message):
    await msg.answer('Находи курьера на астеройде...', reply_markup= reply_key.kb_order)

async def make_order(msg: types.Message):
    await msg.answer('Сделать зака')

async def find_orders(msg: types.Message):
    await msg.answer('найти зака')

async def profile(msg: types.Message):
    await msg.answer('Профиль')
