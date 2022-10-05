import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import django
django.setup()
# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()

from config.settings.base import CAFE, DATA_DIR, CSV_DATA_PATH
from config.settings.local import DB_USER, DATABASES, HEADERS
from datetime import datetime
import psycopg2
from common.conn_db import connect_db
import json

# print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# def test_func(args=()):
#     print(args)


# conn, cur = connect_db()


# def get_cafe_data():
    # for area in CAFE['AREA']:
    #     file_name =  area + '_' + '카페 정보' + '.json'
    #     with open(os.path.join(CAFE['CRAWL_DATA_PATH'], file_name), 'r', encoding='utf-8') as file:
    #         json_data = json.load(file)


class InsertData():
    def insert_cafe(self):
        from cafe.models import Original
        for area in CAFE['AREAS']:
            file_name =  area + '_' + '카페 정보' + '.json'
            try:
                with open(os.path.join(CAFE['CRAWL_DATA_PATH'], file_name), 'r', encoding='utf-8') as file:
                    json_data = json.load(file)
                    # print(json_data)
                    for data in json_data:
                        id = data['id']
                        place_name = data['place_name']
                        address_name = data['address_name']
                        road_address_name = data['road_address_name']
                        phone = data['phone']
                        category_group_name = data['category_group_name']
                        category_name = data['category_name']
                        place_url = data['place_url']

                        Original.objects.create(
                            id=id, place_name=place_name, address_name=address_name, road_address_name=road_address_name,
                            phone=phone, category_group_name=category_group_name, category_name=category_name, place_url=place_url
                        )
            except FileNotFoundError:
                pass



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
    insert_data = InsertData()
    insert_data.insert_cafe()
