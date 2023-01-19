
from aiogram import types,Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from ..button import *


Register_status = 0


def set_state(dp: Dispatcher):
    dp.register_message_handler(register_name, text = "Пройти регистрацию", state = None)
    dp.register_message_handler(Stop_register, text = 'Отмена', state = '*')
    dp.register_message_handler(register_name_complete, state = FSM_Register.name)
    dp.register_message_handler(register_password_complete, state = FSM_Register.password)






class FSM_Register(StatesGroup):
    name = State()
    password = State()
    account = State()


async def register_name(msg: types.Message):
    #state machine
    await FSM_Register.name.set()
    await msg.answer('Введите ваше имя')
    await msg.delete()

async def Stop_register(msg: types.Message, state : FSMContext):
    #state machine
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await msg.answer("Отменяю", reply_markup = reply_key.kb_menu)

async def register_name_complete(msg: types.Message):
    #state machine
    # async with state.proxy() as data:
    #     data ['photo'] = message.name[0].file_id
    await FSM_Register.next()
    await msg.answer('Введите ваш пароль')
    await msg.delete()

async def register_password_complete(msg: types.Message, state : FSMContext):
    #state machine
    await msg.answer('Регистрация завершена', reply_markup = reply_key.kb_menu )
    global Register_status
    Register_status = Register_status + 1
    await msg.delete()
    await state.finish()


