from bs4 import BeautifulSoup
import requests

lotto_url = 'https://dhlottery.co.kr/gameResult.do?method=byWin'
raw = requests.get(lotto_url)

soup = BeautifulSoup(raw.text, "html.parser") # 문자열 타입 HTML(raw.text)를 HTML 코드로 변환

box = soup.find("div", {"class":"nums"}) # <div class="nums">의 큰 영역 지정
numbers = box.find_all("span") # <div class="nums"> 안의 <span>에 해당하는 태그 HTML추출

print("< 최근 로또 당첨 번호 >")
for number in numbers:
    print(number.text) # HTML 코드의 텍스트 데이터 출력
# print(raw.text)
# print(soup)
# print(type(raw.text)) # <class 'str'>
# print(type(soup)) # <class 'bs4.BeautifulSoup'>