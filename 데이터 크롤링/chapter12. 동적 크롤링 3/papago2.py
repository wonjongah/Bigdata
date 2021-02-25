from selenium import webdriver
import time
import csv

driver = webdriver.Chrome("../chromedriver")
papago_url = "https://papago.naver.com"
driver.get(papago_url)
time.sleep(3)

# 읽어올 my_papago.csv 파일을 변수 f에 저장
f = open("./my_papago.csv", "r")

# csv 파일의 모든 데이터를 변수 rdr에 저장
rdr = csv.reader(f)

# rdr의 첫 번째 열 제목은 건너뜀
next(rdr)

# 딕셔너리 생성
my_dict = {}

# 딕셔너리 영단어와 번역 결과를 모두 저장
for row in rdr:
    keyword = row[0]
    korean = row[1]
    my_dict[keyword] = korean

# 파일 닫기
f.close()

# 추가 옵션 a를 사용해 파일 다시 열기
f = open("./my_papago.csv", "a", newline="")
wtr = csv.writer(f)

# while문 안에 있는 조건문을 확인한다
while True:
    keyword = input("번역할 영단어 입력 (0을 입력하면 종료) : ")
    if keyword == "0":
        print("번역종료")
        break

    # 영단어가 my_dict의 키 값 중에 있다면 이 사실을 알려주고 저장되어 있던 번역 결과 출력
    if keyword in my_dict.keys():
        print("이미 번역한 영단어입니다! 뜻은", my_dict[keyword], "입니다.")
    # 위의 경우 포함되어 있지 않으면, 딕셔너리와 csv 파일에 추가
    else:
        driver.find_element_by_css_selector("textarea#txtSource").send_keys(keyword)
        driver.find_element_by_css_selector("button#btnTranslate").click()
        time.sleep(1)

        output = driver.find_element_by_css_selector("div#txtTarget").text

        # csv 파일에 행 추가
        wtr.writerow([keyword, output])
        
        # 딕셔너리에 추가
        my_dict[keyword] = output

        driver.find_element_by_css_selector("textarea#txtSource").clear()

driver.close()
f.close()