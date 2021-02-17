from bs4 import BeautifulSoup
import requests

hankyung_url = 'https://search.hankyung.com/apps.frm/search.news?query=%EC%BD%94%EB%A1%9C%EB%82%98&mediaid_clust=HKPAPER,HKCOM&page=1'
raw = requests.get(hankyung_url)

soup = BeautifulSoup(raw.text, "html.parser") # 문자열 타입 HTML(raw.text)를 HTML 코드로 변환

box = soup.find("ul", {"class":"article"}) # <div class="nums">의 큰 영역 지정
date_time = box.find_all("span", {"class":"date_time"}) # <div class="nums"> 안의 <span>에 해당하는 태그 HTML추출
title = box.find_all("em", {"class":"tit"})
print("< 최근 기사 제목과 작성 날짜 >\n")
for tit, date in zip(title, date_time):
    print(tit.text.strip(), date.text.strip()) # HTML 코드의 텍스트 데이터 출력