from aiogram import types,Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from ...create_bot import *

from ..button import *
from ...database.utils import *
from ...parser import get_data
from ...database.utils import *

import json

class FSM_Order(StatesGroup):
    register_order = State()
    choose_order = State()

def set_state_order(dp: Dispatcher):
    dp.register_message_handler(order_start, text = "Сделать Заказ", state = None)
    dp.register_message_handler(order_register, text= FSM_Order.register_order)
    dp.register_message_handler(order_register, text= FSM_Order.choose_order)

async def order_start(msg: types.Message):
    await FSM_Order.register_order.set()
    
    json_orders = get_data('https://yaponomaniya.com/assorty')
    call_answer = None
    await msg.answer("Товары:")

    with open(json_orders, 'r', encoding='utf-8') as f:
        data = list(json.load(f).items())
        for order in data:
            items_string = "\n" + str(order[0]) + "\n    " + order[-1]['cost'] + '\n    ' + order[-1]['desc'] +"\n"

            button= InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton(text = "Сделать Заказ", callback_data=f"{order[0]}"))
            call_answer = await msg.answer(items_string, reply_markup=button)

        for order in data:
            async def callback(call: types.CallbackQuery):
                await call.message.answer("Ваш заказ очень важен для нас")
                await bot.delete_message(call.message.from_user.id, call_answer.message_id)
                # for answer in answers:
                #     answer.delete()
            
            dp.register_callback_query_handler(callback, text= f'{order[0]}')
    
    

async def order_register(msg: types.Message, state: FSMContext):
    print(msg.text)
    await state.finish()