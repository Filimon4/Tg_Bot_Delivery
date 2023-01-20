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

    await msg.answer("Товары:")

    with open(json_orders, 'r', encoding='utf-8') as f:
        data = list(json.load(f).items())
        calls = []
        for order in data:
            name = str(order[0])
            items_string = "\n" + str(order[0]) + "\n    " + order[-1]['cost'] + '\n    ' + order[-1]['desc'] +"\n"

            button= InlineKeyboardMarkup(row_width=1, inline_keyboard = [
                [InlineKeyboardButton(text = "Оформить Заказ", callback_data= name)]
            ])
            await bot.send_photo(msg.chat.id, photo=str(order[-1]['img']))
            await msg.answer(items_string, reply_markup=button)
            calls.append(name)

        for name in calls:
            print(name)
            async def call(callback_query: types.CallbackQuery):
                await call.message.answer('He')

            dp.register_callback_query_handler(call, text= name)

async def order_register(msg: types.Message, state: FSMContext):
    await FSM_Order.next()
    await state.finish()