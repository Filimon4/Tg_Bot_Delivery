
from aiogram import types,Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from ..button import *
from ...database.utils import *
from aiogram import Bot
import os

class FSM_Review(StatesGroup):
    review = State()

def set_state_review(dp: Dispatcher):
    dp.register_message_handler(review_register, text= '🤝написать отзыв', state = None)
    dp.register_message_handler(review_register_complete, state = FSM_Review.review)
    dp.register_message_handler(stop_review, text = 'Назад', state = '*')

async def review_register(msg: types.Message):
    #state machine2
    await FSM_Review.review.set()
    await msg.answer('Напишите свой отзыв', reply_markup = reply_key.kb_review )

async def stop_review(msg: types.Message, state : FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await msg.answer("Отменяю", reply_markup = reply_key.kb_menu)

async def review_register_complete(msg: types.Message, state : FSMContext):
    #state machine2
    answer = msg.text
    try:
        if str(answer):
            bot = Bot(token=os.getenv("TOKEN"))
            async with state.proxy() as data:
                data['text'] = msg.text
            await msg.answer('Ваш отзыв принят', reply_markup = reply_key.kb_menu )
            await bot.send_sticker(chat_id=msg.from_user.id,
                           sticker="CAACAgIAAxkBAAEHWh1jyjrBRrLl7U52j3gftuH8XlthXQACnhUAAupMsUhJMmE2oQ35GS0E")
            data = await state.get_data()
            set_review(data)
            await state.finish()
        else:
            msg.answer("Введите корректно")
            await bot.send_sticker(chat_id=msg.from_user.id,
                           sticker="CAACAgIAAxkBAAEHWhdjyjp-Bac8iI5WuL2eTZ55R2r7EAACwRMAAl0nsUh_DkCx1ZLahS0E")
    except Exception:
        msg.answer("Введите корректно")