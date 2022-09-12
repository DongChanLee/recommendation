import os
from datetime import datetime
from .base import *
from dotenv import load_dotenv

load_dotenv()

# BASE_DIR = '/Users/dc/study_dir/recommendation'

ALLOWED_HOSTS = []

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# [DB]
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DB_USER = 'dc'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}