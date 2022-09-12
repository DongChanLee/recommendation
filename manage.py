#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from dotenv import load_dotenv

# load_dotenv('../.env')
load_dotenv()

def main():
    envstate = os.getenv('ENV_STATE','local')
    if envstate=='production':   # 상용
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.production')
    elif envstate=='development':   # 개발용
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')
    else:   # 로컬용
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
# 출처: https://engineer-mole.tistory.com/299

# def main():
#     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
#     try:
#         from django.core.management import execute_from_command_line
#     except ImportError as exc:
#         raise ImportError(
#             "Couldn't import Django. Are you sure it's installed and "
#             "available on your PYTHONPATH environment variable? Did you "
#             "forget to activate a virtual environment?"
#         ) from exc
#     execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
