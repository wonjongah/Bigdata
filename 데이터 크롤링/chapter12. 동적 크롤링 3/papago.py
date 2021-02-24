from selenium import webdriver
import time
import csv

driver = webdriver.Chrome("../chromedriver")

papago_url = "https://papago.naver.com/"
driver.get(papago_url)

time.sleep(3)

f = open("./my_papago.csv", "w", newline="")
# csv 파일 작성하는 객체 변수 wtr
wtr = csv.writer(f)

wtr.writerow(["영단어", "번역결과"])

while True:
    keyword = input("번역할 영단어 입력 (0 입력 시 종료) : ")
    if keyword == "0":
        print("번역 종료")
        break

    driver.find_element_by_css_selector("textarea#txtSource").send_keys(keyword)
    driver.find_element_by_css_selector("button#btnTranslate").click()
    time.sleep(1)

    output = driver.find_element_by_css_selector("div#txtTarget").text
    
    wtr.writerow([keyword, output])
    driver.find_element_by_css_selector("textarea#txtSource").clear()

driver.close()
f.close()