import enum
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.settings.base import CAFE, DATA_DIR, CSV_DATA_PATH
from config.settings.local import DB_USER, DATABASES, HEADERS
from datetime import datetime
import psycopg2
from common.conn_db import connect_db

# print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# def test_func(args=()):
#     print(args)


conn, cur = connect_db()

class InsertData():
    def insert_cafe(self):
        



# def select_execute(query, args=(), one=False): 
#     '''
#     select 쿼리 수행 함수
#     one=False -> 단일 결과가 아닌 복수 결과를 받아오는 것을 의미
#     '''
#     cur.execute(query, args)

#     for i, value in enumerate(row):
#         for row in cur.fetchall():
#             result = dict(cur.description[i][0], value)



#     result = for i, value in enumerate(row)


# def query_db(query, args=(), one=False):
# 	cur = db().cursor()
# 	#cur.set_client_encoding('UTF8')
# 	cur.execute(query, args)
# 	r = [dict((cur.description[i][0], value) \
# 		for i, value in enumerate(row)) for row in cur.fetchall()]
# 	cur.connection.close()
# 	return (r[0] if r else None) if one else r

# def insert_query_db(query, args=(), one=False):
# 	conn = db()
# 	cur = conn.cursor()
# 	cur.execute(query, args)
# 	conn.commit()


if __name__ == '__main__':
    # test_func()
