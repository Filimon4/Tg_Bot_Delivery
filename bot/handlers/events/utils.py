from aiogram import types

from ..button import *

async def start(msg: types.Message):
    await msg.answer("Здравствуйте, вас приветсвует бот Акио для заказов еды из Япономании", reply_markup=reply_key.kb_menu)
    #await msg.delete()

async def register(msg: types.Message):
    #state machine
    await msg.answer('Регистрация не готова =)')
    await msg.delete()

async def order(msg: types.Message):
    await msg.answer('Заказы ещё не готовы')
    await msg.delete()