from peewee import *
from .model import *

def set_user(data):
    try:
        User.create(
            user_id = data['user_id'],
            mail = data['email'][-1],
            phone = data['phone'],
        )
    except Exception:
        print('Something went wrong with creating')


def get_user(id_user):
    user = User().select().where(User.user_id == id_user)
    return True if user else False

def set_order(data):
    try:
        Order.create(
            
        )
    except IndexError:
        print("That order is denied")

def delete_order():
    pass

def set_review(data):
    print(data)
    try:
        Review.create(
            review = data['text']
        )
    except IndexError:
        print("There is problem with review")

def get_revew():
    pass