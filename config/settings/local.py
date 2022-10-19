import os
from datetime import datetime
from .base import *
from dotenv import load_dotenv

load_dotenv()

ALLOWED_HOSTS = []

DEBUG = True

# [DB]
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DB_USER = 'dc'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'recommendation',
        'USER': DB_USER,
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': os.environ['DB_HOST_LOCAL'],
        'PORT': os.environ['DB_PORT_LOCAL'],
    }
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Authorization": "KakaoAK" + " " + os.environ['API_KEY_KAKAO']
}

# API_KEY_KAKAO = os.environ['API_KEY_KAKAO']

# print(f'API KEY KAKAO: {API_KEY_KAKAO}')
# print(f'DATABASE HOST 정보: {DATABASES["default"]["HOST"]}')
# print(f'DATABASE PW정보: {DATABASES["default"]["PASSWORD"]}')
