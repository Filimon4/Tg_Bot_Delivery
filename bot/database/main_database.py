from aiogram import types, Dispatcher
from .models import *

def start_database(dp: Dispatcher):
    db.connect()
    with db:
        db.create_tables([User,Order])