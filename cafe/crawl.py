import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pandas as pd
import numpy as np
import json
from config.settings.base import CAFE, DATA_DIR, CSV_DATA_PATH
from config.settings.local import HEADERS
from datetime import datetime
import requests
import time

# print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 'https://dapi.kakao.com/v2/local/search/keyword.json?page=1&size=15&sort=accuracy&query=%EA%B0%95%EB%82%A8%EA%B5%AC+%EC%B9%B4%ED%8E%98&category_group_code=CE7'

#areas = ['종로구']
areas = ['종로구', '중구', '용산구', '성동구', '광진구', 
         '동대문구', '중랑구', '성북구', '강북구', '도봉구', 
         '노원구', '은평구', '서대문구', '마포구', '양천구', 
         '강서구', '구로구', '금천구', '영등포구', '동작구', 
         '관악구', '서초구', '강남구', '송파구', '강동구']

url = 'https://dapi.kakao.com/v2/local/search/keyword.json'

def get_cafe_info():
    data = []
    for area in areas:
        for i in range(1, 3):  # 최대 page=45
            params = {'page': i, 'size': 15, 'query': area, 'category_group_code': 'CE7'}
            res = requests.get(url=url, params=params, headers=HEADERS, verify=False)
            res.encoding = 'utf-8'
            res = res.json()       
            for j in res['documents']:
                new_data = {
                    'id': j['id'], 'place_name': j['place_name'], 'address_name': j['address_name'], 
                    'road_address_name': j['road_address_name'], 'phone': j['phone'], 
                    'category_group_name': j['category_group_name'], 'category_name': j['category_name'], 'place_url': j['place_url'] 
                }
                data.append(new_data)            
        file_name = area + '_' + '카페 정보' + '.json'
        with open(os.path.join(CAFE['CRAWL_DATA_PATH'], file_name), 'w', encoding='utf-8') as file:
            file.write(json.dumps(data, indent=4, ensure_ascii=False))
        time.sleep(0.5)


def json_to_csv():
    df = pd.read_json(os.path.join(CAFE['CRAWL_DATA_PATH'], '종로구_카페 정보.json'))
    df.to_csv(os.path.join(CAFE['CSV_DATA_PATH'], '종로구_카페 정보.csv'))


def get_blog_review():
    '''
    네이버 블로그 리뷰 크롤링
    참고: https://data101.oopy.io/recommendation-engine-cosine-similarity-naver-version-code-sharing
    '''
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import TimeoutException
    from selenium.common.exceptions import NoSuchElementException
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import Select

    # 작성 당시 크롬 버젼 : 106.0.5249.103
    chromedriver = '/Users/dc/practice/recommendation/recomm_drf/cafe/chromedriver' 
    driver = webdriver.Chrome(chromedriver) 
    
    # csv 파일 import
    df = pd.read_csv(os.path.join(CSV_DATA_PATH, '종로구_카페 정보.csv'), sep=',')

    # 네이버 지도 검색창에 [~동 @@식당]으로 검색해 정확도를 높여야 합니다. 검색어를 미리 설정해줍시다.
    df['dong'] = df.iloc[:, 3].str.split(' ').str[1]
    df['naver_keyword'] = df['dong'] + '%20' + df['place_name']
    df['naver_map_url'] = ''
    # # ==============================================
    # df['naver_keyword'] = df['dong'] + "%20" + df['name']  # "%20"는 띄어쓰기를 의미합니다.
    # df['naver_map_url'] = ''

    # 본격적으로 가게 상세페이지의 URL을 가져옵시다
    for i, keyword in enumerate(df['naver_keyword'].tolist()):
        print(f'이번에 찾을 키워드 : {i}행 / 전체 {df.shape[0] -1}행중 {keyword}')
        if ' ' in keyword:
            join_keyword = ''.join(keyword.split())
        else:
            join_keyword = keyword
        try:
            naver_map_search_url = f"https://m.map.naver.com/search2/search.naver?query={join_keyword}&sm=hty&style=v5"
            
            driver.get(naver_map_search_url)
            time.sleep(1.5)
            df.iloc[i,-1] = driver.find_element(By.CSS_SELECTOR, '#ct > div.search_listview._content._ctList > ul > li > div.item_info > a.a_item.a_item_distance._linkSiteview').get_attribute('data-cid')
            # 네이버 지도 시스템은 data-cid에 url 파라미터를 저장해두고 있었습니다.
            # data-cid 번호를 뽑아두었다가 기본 url 템플릿에 넣어 최종적인 url을 완성하면 됩니다.
            
            #만약 검색 결과가 없다면?
        except Exception as e:
            print(e)
            pass
    driver.quit()

    # 이때 수집한 것은 완전한 URL이 아니라 URL에 들어갈 ID (data-cid 라는 코드명으로 저장된) 이므로, 온전한 URL로 만들어줍니다
    df['naver_map_url'] = "https://m.place.naver.com/restaurant/" + df['naver_map_url']

    # URL이 수집되지 않은 데이터는 제거합니다.
    df = df.loc[df['naver_map_url'] != 'https://m.place.naver.com/restaurant/']
    # df = df.loc[~df['naver_map_url'].isnull()]

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

if __name__ == "__main__": 
    # get_cafe_info_test()
    get_cafe_info()
    # json_to_csv()
    # get_blog_review()