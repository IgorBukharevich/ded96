import os
from peewee import *
from dotenv import load_dotenv

load_dotenv()

# CONFIG FLASK APP/SECRET CEY
KEY_FLASK = os.getenv('KEY_FLASK')


# CONFIG CONNECTION DATABASE - Postgresql
db = PostgresqlDatabase(
    database=os.getenv('NAME_DB'),
    user=os.getenv('USER_DB'),
    password=os.getenv('PASSWORD_DB'),
    host=os.getenv('HOST_DB'),
    port=os.getenv('PORT_DB'),
)
