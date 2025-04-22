from peewee import *
import bcrypt
from database.database import db

class User(Model):
    name = CharField(max_length=100)
    email = CharField(unique=True)
    password = CharField(max_length=16)

    class Meta:
        database = db

        
