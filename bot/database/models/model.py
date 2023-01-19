from peewee import *

db = SqliteDatabase("Bot.db")

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    pass

class Order(BaseModle):
    pass