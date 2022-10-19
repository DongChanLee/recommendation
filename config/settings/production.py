import os
from datetime import datetime
from .base import *
from dotenv import load_dotenv

load_dotenv()

# ALLOWED_HOSTS = ['3.37.58.70']


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


# [DB]
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DB_USER = ''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}