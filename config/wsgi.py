"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from dotenv import load_dotenv


application = get_wsgi_application()

# load_dotenv('../.env')
load_dotenv()

envstate = os.getenv('ENV_STATE','local')
if envstate=='production':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.production')
elif envstate=='development':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
#  출처: https://engineer-mole.tistory.com/299




# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# application = get_wsgi_application()
