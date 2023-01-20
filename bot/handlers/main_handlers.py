from aiogram import types, Dispatcher

from .events import *
from .callback import *
from .state import *

def set_handlers(dp: Dispatcher):
    set_events(dp)
    set_state_register(dp)
    set_state_review(dp)