from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from ..button import *

async def start(msg: types.Message):
    await msg.answer("Здравствуйте, вас приветсвует бот Акито для заказов еды из Япономании", reply_markup=reply_key.kb_menu)
    await msg.delete()

async def register(msg: types.Message):
    #check database
    
    await msg.answer('Ищю межпланетного диспечера...', reply_markup= reply_key.kb_register)

async def cancel_register(msg: types.Message):
    await msg.answer('Возращаю', reply_markup= reply_key.kb_menu)

async def order(msg: types.Message):
    await msg.answer('Находи курьера на астеройде...', reply_markup= reply_key.kb_order)

async def make_order(msg: types.Message):
    await msg.answer('Сделать зака')

async def find_orders(msg: types.Message):
    await msg.answer('найти зака')

async def profile(msg: types.Message):
    await msg.answer('Находим данные с комет...', reply_markup= reply_key.kb_profile)

async def find_points(msg: types.Message):
    await msg.answer('Выводим кол-во поинтов...')
