from selenium import webdriver
import time
import csv

driver = webdriver.Chrome("../chromedriver")
papago_url = "https://papago.naver.com"
driver.get(papago_url)
time.sleep(3)

# 영어 - 한국어 버튼 한 번만 클릭
driver.find_element_by_css_selector("button.btn_switch___x4Tcl").click()

# csv 파일의 한국어만 따로 저장
f = open("./my_papago.csv", "r", newline="")
rdr = csv.reader(f)
next(rdr)

# 한글 번역 결과 저장 리스트
korean = []
for r in rdr:
    korean.append(r[1])

# 이전과 똑같이 입력 - 번역 버튼 클릭 - 번역 결과 출력

# while문 안에 있는 조건문을 확인한다
for k in korean:
    driver.find_element_by_css_selector("textarea#txtSource").send_keys(k)
    driver.find_element_by_css_selector("button#btnTranslate").click()
    time.sleep(1)

    output = driver.find_element_by_css_selector("div#txtTarget").text
    print(f"{k} : {output}")
    driver.find_element_by_css_selector("textarea#txtSource").clear()

driver.close()
f.close()