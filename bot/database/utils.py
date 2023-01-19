from peewee import *
from .model import *

def create_user():
    try:
        User(
            
        ).save()
    except InterityError:
        print("That user is already exist")

def create_order():
    try:
        Order.create(

        )
    except IndexError:
        print("That order is denied")

