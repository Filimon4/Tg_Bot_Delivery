
from aiogram import types,Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from ..button import *


class FSM_Review(StatesGroup):
    review = State()

def set_state2(dp: Dispatcher):
    dp.register_message_handler(review_register, text= '🤝напишите отзыв', state = None)
    dp.register_message_handler(review_register_complete, state = FSM_Review.review)

async def review_register(msg: types.Message):
    #state machine2
    await FSM_Review.review.set()
    await msg.answer('Напишите свой отзыв')
    await msg.delete()

async def review_register_complete(msg: types.Message, state : FSMContext):
    #state machine2
    await msg.answer('Ваш отзыв принят', reply_markup = reply_key.kb_menu )
    await msg.delete()
    await state.finish()