from aiogram import types, Dispatcher

from .voice import *
from .events import *
from .callback import *
from .state import *

def set_handlers(dp: Dispatcher):
    set_events(dp)
    registr_voice(dp)
    set_state(dp)