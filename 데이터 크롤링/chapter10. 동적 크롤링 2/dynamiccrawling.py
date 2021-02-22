from selenium import webdriver
import time

# 자동화된 크롬 창 실행
driver = webdriver.Chrome("../chromedriver")

# 파파고 웹 페이지 접속
papago_url = "https://papago.naver.com/"
driver.get(papago_url)
# 시간적 여유 3초
time.sleep(3)

question = input("번역할 영단어 입력 : ")

# 영단어 자동 입력
driver.find_element_by_css_selector("textarea#txtSource").send_keys(question)
# 해당 버튼 클릭
driver.find_element_by_css_selector("button#btnTranslate").click()
time.sleep(1)
# 번역 결과 text 저장, 출력
output = driver.find_element_by_css_selector("div#txtTarget").text
print("번역 결과 :", output)

# 크롬 창 닫기
driver.close()