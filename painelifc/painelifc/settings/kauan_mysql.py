# coding=utf-8
'''
Configurações do mysql
'''
from base import *

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.mysql",
        # DB name or path to database file if using sqlite3.
        "NAME": "painelifc2",
        # Not used with sqlite3.
        "USER": "root",
        # Not used with sqlite3.
        "PASSWORD": "root",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "localhost",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "3306",
    }
}

# ============================
