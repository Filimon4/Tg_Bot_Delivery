from aiogram import types,Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from ..button import *
from ...database.utils import *

class FSM_Register(StatesGroup):
    email = State()
    phone = State()

def set_state_register(dp: Dispatcher):
    
    dp.register_message_handler(register_start, text = "Пройти регистрацию", state = None)
    
    dp.register_message_handler(stop_register, text = 'Отмена', state = '*')
    
    dp.register_message_handler(register_email, state = FSM_Register.email)
    dp.register_message_handler(register_phone, state = FSM_Register.phone)
    

async def register_start(msg: types.Message):
    user = get_user(msg.from_user.id)
    if not user:
        await FSM_Register.email.set()
        await msg.answer('Введите ваш email')
    else:
        await msg.answer("Вы уже зарегистрировались", reply_markup = reply_key.kb_menu)

async def register_email(msg: types.Message, state : FSMContext):
    await FSM_Register.next()

    try:
        if "@" in msg.text :
            async with state.proxy() as data:
                data['user_id'] = msg.from_user.id
                data['email'] = msg.text.split()
            await msg.answer('Введите ваш номер телефона')

        else:
            await msg.answer("Введите корректный email")
    except Exception:
        await msg.answer("Введите корректный email")

async def register_phone(msg: types.Message, state : FSMContext):
    answer = msg.text.replace('+',"").replace('-','')
    try:
        if answer.isnumeric():
            await state.update_data(phone = answer)
            await msg.answer('Регистрация завершена', reply_markup = reply_key.kb_menu )
            data = await state.get_data()
            set_user(data)
            print("finished")
            await state.finish()
        else:
            await msg.answer("Введите корректный номер телефона")
    except Exception:
        print('Введите корректный номер телефона')


async def stop_register(msg: types.Message, state : FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await msg.answer("Отменяю", reply_markup = reply_key.kb_menu)