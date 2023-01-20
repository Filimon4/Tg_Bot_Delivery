from aiogram import types,Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from ..button import *
from ...database.utils import *
from ...parser import get_data

class FSM_Order(StatesGroup):
    register_order = State()

def set_state_order(dp: Dispatcher):
    
    dp.register_message_handler(register_order, text = "Сделать Заказ", state = None)

async def register_order(msg: types.Message):
    await FSM_Order.register_order.set()
    print(get_data)
    await msg.answer (get_data)





