import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pandas as pd
import numpy as np
import json
from config.settings.base import CAFE, DATA_DIR, CSV_DATA_PATH



# csv 파일 import
df = pd.read_csv(os.path.join(CSV_DATA_PATH, '종로구_카페 정보.csv'), sep=',')


df['naver_keyword'] = df['']
df['naver_map_url'] = ''