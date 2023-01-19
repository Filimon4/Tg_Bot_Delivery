from peewee import *

db = SqliteDatabase("Bot.db")

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    user_id = CharField(unique=True)

    class Meta:
        table_name = "Users",

class Order(BaseModel):
    from_user = ForeignKeyField(User, backref="relationship")
    order_name = CharField()
    order_cost = FloatField()

    class Meta:
        table_name = "Orders"