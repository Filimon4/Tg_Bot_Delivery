from aiogram import types, Dispatcher
from .model import *
from .utils import *

def start_database(dp: Dispatcher):
    db.connect()
    db.create_tables([User,Order,Review], safe=True)