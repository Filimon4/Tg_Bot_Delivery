from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from ..button import *

async def start(msg: types.Message):
    await msg.answer("Здравствуйте, вас приветсвует бот для заказов еды", reply_markup=reply_key.kb_menu)
    await msg.delete()

async def register(msg: types.Message):
    #state machine
    await msg.answer('Регистрация не готова =)', reply_markup= reply_key.Register)
    await msg.delete()

async def cancel_register(msg: types.Message):
    await msg.answer('Возращаю', reply_markup= reply_key.kb_menu)
    await msg.delete()


async def order(msg: types.Message):
    await msg.answer('Регистрация не готова =)')
    await msg.delete()
