import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.settings.local import DB_USER, DATABASES
import psycopg2

def connect_db():
    try:
        conn = psycopg2.connect(
                host = DATABASES['default']['HOST'],
                port = DATABASES['default']['PORT'],
                database = DATABASES['default']['NAME'],
                user = DATABASES['default']['USER'],
                password = DATABASES['default']['PASSWORD'])
    except psycopg2.DatabaseError as e:
        print(f'DB 연동 오류 발생: {e}')
    else:
        cur =  conn.cursor()
        print(f'DB 연결 성공')
    return conn, cur