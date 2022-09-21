import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import json
from config.settings.base import CAFE
from config.settings.local import HEADERS
from datetime import datetime
import requests
import time

# print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 'https://dapi.kakao.com/v2/local/search/keyword.json?page=1&size=15&sort=accuracy&query=%EA%B0%95%EB%82%A8%EA%B5%AC+%EC%B9%B4%ED%8E%98&category_group_code=CE7'

areas = ['종로구']
# areas = ['종로구', '중구', '용산구', '성동구', '광진구', '동대문구', '중랑구', '성북구', '강북구', '도봉구', '노원구', '은평구', 
#         '서대문구', '마포구', '양천구', '강서구', '구로구', '금천구', '영등포구', '동작구', '관악구', '서초구', '강남구', '송파구', '강동구']

url = 'https://dapi.kakao.com/v2/local/search/keyword.json'

def get_cafe_info():
    for area in areas:
        for i in range(1, 3):  # 최대 page=45
            params = {'page': i, 'size': 15, 'query': area, 'category_group_code': 'CE7'}
            res = requests.get(url=url, params=params, headers=HEADERS, verify=False)
            res.encoding = 'utf-8'
            
            time.sleep(0.5)

            file_name = area + '_' + '카페 정보' + '(' + str(i) + ')'+ '.json'
            with open(os.path.join(CAFE['CRAWL_DATA_PATH'], file_name), 'w', encoding='utf-8') as file:
                json.dump(res.json(), file, indent='\t', ensure_ascii=False)

            # print(f'{area} 카페 리스트')
            # print(f'{response.json()}')

    # params = {'page': 2, 'size': 15, 'sort': 'accuracy', 'query': '도봉구 카페', 'category_group_code': 'CE7'}





    # print(res.json())
    # print(response.encoding)
    # print(response.status_code)
    # print(HEADERS)


def get_cafe_info2():
    data=[]
    for area in areas:
        for i in range(1, 3):  # 최대 page=45
            params = {'page': i, 'size': 15, 'query': area, 'category_group_code': 'CE7'}
            res = requests.get(url=url, params=params, headers=HEADERS, verify=False)
            res.encoding = 'utf-8'
            res = res.json()
            
            for i in res['documents']:
                new_data = {
                    'id': i['id'],  'place_name': i['place_name'],  'address_name': i['address_name'], 'road_address_name': i['road_address_name'], 
                    'phone': i['phone'], 'category_group_name': i['category_group_name'], 'category_name': i ['category_name'], 'place_url': i['place_url'] 
                }

            file_name = area + '_' + '카페 정보_가공' + '(' + str(i) + ')'+ '.json'
            with open(os.path.join(CAFE['CRAWL_DATA_PATH'], file_name), 'w', encoding='utf-8') as file:
                json.dump(res.json(), file, indent='\t', ensure_ascii=False)
            
            time.sleep(0.5)

if __name__ == "__main__": 
    # get_cafe_info()
    get_cafe_info2()