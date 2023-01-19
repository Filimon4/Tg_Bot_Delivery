from aiogram import types, Dispatcher

from .events import *
from .callback import *

def set_handlers(dp: Dispatcher):
    set_events(dp)