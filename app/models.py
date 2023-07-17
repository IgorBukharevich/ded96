from peewee import *

from app.config_db import db


class DataJson(Model):

    name = CharField(max_length=50)
    date = DateTimeField()

    class Meta:
        database = db
