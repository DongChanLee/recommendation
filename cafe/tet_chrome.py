import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# [크롬드라이버 최신 버전 자동 설치 모듈]
# from selenium import webdriver
# import chromedriver_autoinstaller

# chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]  #크롬드라이버 버전 확인

# try:
#     driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe')   
# except:
#     chromedriver_autoinstaller.install(True)
#     driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe')

# driver.implicitly_wait(10)

driver = webdriver.Chrome(executable_path='/Users/dc/practice/recommendation/recomm_drf/cafe/chromedriver')