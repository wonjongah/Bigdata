from selenium import webdriver
# selenium 라이브러리의 webdriver 함수 임포트
import time

driver = webdriver.Chrome("../chromedriver")
# webdriver에 chromedriver.exe를 연결한 객체를 생성한다.
# 가상의 크롬 창을 열 수 있도록 도와주는 속성값과 행동을 driver 변수에
papago_url = "https://papago.naver.com/"
driver.get(papago_url)

time.sleep(3)
driver.close()