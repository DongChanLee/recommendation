import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import json
from config.settings.local import HEADERS
from datetime import datetime
import requests

# print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 'https://dapi.kakao.com/v2/local/search/keyword.json?page=1&size=15&sort=accuracy&query=%EA%B0%95%EB%82%A8%EA%B5%AC+%EC%B9%B4%ED%8E%98&category_group_code=CE7'

url = 'https://dapi.kakao.com/v2/local/search/keyword.json'
params = {'page': 1, 'size': 15, 'sort': 'accuracy', 'query': '도봉구 카페', 'category_group_code': 'CE7'}

response = requests.get(url=url, params=params, headers=HEADERS)


print(response.json())
print(response.encoding)
print(response.status_code)
# print(HEADERS)