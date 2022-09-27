import os
import sys
from unittest import result
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pandas as pd
import json
from config.settings.base import CAFE, DATA_DIR, CSV_DATA_PATH
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

def get_cafe_info_test():
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


# def get_cafe_info_error():
#     data = []
#     for area in areas:
#         for i in range(1, 3):  # 최대 page=45
#             params = {'page': i, 'size': 15, 'query': area, 'category_group_code': 'CE7'}
#             res = requests.get(url=url, params=params, headers=HEADERS, verify=False)
#             res.encoding = 'utf-8'
#             res = res.json()
            
#             for j in res['documents']:
#                 new_data = {
#                     'id': j['id'], 'place_name': j['place_name'], 'address_name': j['address_name'], 'road_address_name': j['road_address_name'], 
#                     'phone': j['phone'], 'category_group_name': j['category_group_name'], 'category_name': j['category_name'], 'place_url': j['place_url'] 
#                 }

#                 data.append(new_data)

#             file_name = area + '_' + '카페 정보' + '.json'
#             with open(os.path.join(CAFE['CRAWL_DATA_PATH'], file_name), 'a', encoding='utf-8') as file:
#                 file.write(json.dumps(data, indent=4, ensure_ascii=False))

#             time.sleep(0.5)

        # df = pd.read_json(os.path.join(CAFE['CRAWL_DATA_PATH'], file_name))
        # df.to_csv(os.path.join(CAFE['CSV_DATA_PATH'], f'{file_name}.csv'))
            

            # file_name = area + '_' + '카페 정보_가공' + '(' + str(i) + ')'+ '.json'
            # with open(os.path.join(CAFE['CRAWL_DATA_PATH'], file_name), 'w', encoding='utf-8') as file:
            #     file.write(json.dumps(data, indent=4, ensure_ascii=False))
            
            

# def json_to_csv():
#     df = pd.read_json(os.path.join(CAFE['CRAWL_DATA_PATH'], '종로구_카페 정보_가공(1).json'))
#     df.to_csv(os.path.join(CAFE['CSV_DATA_PATH'], '종로구_카페 정보_가공(1).csv'))


def get_cafe_info():

    data = []
    result = []
    for area in areas:
        for i in range(1, 3):  # 최대 page=45
            params = {'page': i, 'size': 15, 'query': area, 'category_group_code': 'CE7'}
            res = requests.get(url=url, params=params, headers=HEADERS, verify=False)
            res.encoding = 'utf-8'
            res = res.json()
            
            for j in res['documents']:
                new_data = {
                    'id': j['id'], 'place_name': j['place_name'], 'address_name': j['address_name'], 'road_address_name': j['road_address_name'], 
                    'phone': j['phone'], 'category_group_name': j['category_group_name'], 'category_name': j['category_name'], 'place_url': j['place_url'] 
                }

                data.append(new_data)            
        result = result + data
      
        # print(f'============== 최종 result ==================')
        # print(result)
        file_name = area + '_' + '카페 정보' + '.json'
        with open(os.path.join(CAFE['CRAWL_DATA_PATH'], file_name), 'a', encoding='utf-8') as file:
            file.write(json.dumps(result, indent=4, ensure_ascii=False))

        time.sleep(0.5)

if __name__ == "__main__": 
    # get_cafe_info_test()
    get_cafe_info()
    # json_to_csv()