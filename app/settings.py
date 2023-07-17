import os
from dotenv import load_dotenv

load_dotenv()

# APP FLASK
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')
DEBUG = os.getenv('DEBUG')


# APP DATABASE - Postgresql
DIALECT_DB = os.getenv('DIALECT_DB')
USER_DB = os.getenv('USER_DB')
PASSWORD_DB = os.getenv('PASSWORD_DB')
HOST_DB = os.getenv('HOST_DB')
PORT_DB = os.getenv('PORT_DB')
NAME_DB = os.getenv('NAME_DB')
