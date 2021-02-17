##### 크롤링 대상 사이트 살펴보기



https://search.hankyung.com/apps.frm/search.news?query=%EC%BD%94%EB%A1%9C%EB%82%98&page=2

의 url 패턴을 살펴보면, query="검색값"&page="페이지값"임을 알 수 있다. 

![캡처](https://user-images.githubusercontent.com/50413112/108148822-f3e3a880-7114-11eb-91cd-c8d1ab2ba13e.PNG)

```
<ul class="article">은 기사의 목차를 나타낸다.
<ul class="article">에 속한 <li> 태그는 각 뉴스 기사를 나타낸다.
<li> 태그 속 <em class="tit"> 태그에 뉴스 기사의 제목이 담겨있다.

```

-> ul : unordered list. 목차의 큰 틀이다.

-> li : list item. 목차 하나하나를 나타냄. 목차의 내용.

-> em : 이탤리체 태그 <i>와 외관상 같지만 em 태그는 강조된 텍스트이기 때문에 컴퓨터가 읽어줄 때 강세를 강조하기도 한다.

위의 페이지에서 기사 제목 10개를 검색할 때는 ctrl + F를 누른 뒤 "ul.article em.tit"로 검색하면 제목 10개가 나오는 것을 알 수 있다.



정적 크롤링은 url 주소 하나를 대상으로 크롤링한다.

url 주소 패턴 파악은 여러 개의 url 주소를 대상으로 정적크롤링을 여러번 하기 위함이다.

동적크롤링은 하나의 url 주소에 접속하고, 그 안에서 이동하면서 데이터를 수집한다.



ex)

```python
from bs4 import BeautifulSoup
import requests

hankyung_url = 'https://search.hankyung.com/apps.frm/search.news?query=%EC%BD%94%EB%A1%9C%EB%82%98&mediaid_clust=HKPAPER,HKCOM&page=1'
raw = requests.get(hankyung_url)

soup = BeautifulSoup(raw.text, "html.parser") # 문자열 타입 HTML(raw.text)를 HTML 코드로 변환

box = soup.find("ul", {"class":"article"}) # <ul class="article">의 큰 영역 지정
date_time = box.find_all("span", {"class":"date_time"}) # <ul class="article"> 안의 <span>에 해당하는 태그 HTML추출
title = box.find_all("em", {"class":"tit"})
print("< 최근 기사 제목과 작성 날짜 >\n")
for tit, date in zip(title, date_time):
    print(tit.text.strip(), date.text.strip()) # HTML 코드의 텍스트 데이터 출력
```

```
< 최근 기사 제목과 작성 날짜 >

졸업사진 5인이상 금지? "찍는 건 가능, '구호'는 안돼" 2021.02.17 12:08
'5년간 해외여행 30번' 20대 명품족…비결은 '아빠 회사 돈' 2021.02.17 12:00
자산과열 불쏘시개 됐나...작년 유동성 증가폭 사상 최대 2021.02.17 12:00
정세균·이재명 등 與인사 앞다퉈 中 공산당 기관지에 새해인사 2021.02.17 11:46
나이벡 "상온 보관 mRNA 코로나 백신 공동연구 시작" 2021.02.17 11:42
[한상춘의 세계경제 읽기] 바이든-포스트 코로나 시대의 재테크 2021.02.17 11:38
중고교생도 아동수당 받나…이낙연 이어 복지부도 "확대 검토" 2021.02.17 11:37
기아 새 로고 단 K8 출격 임박…'국민차' 그랜저에 도전 2021.02.17 11:33
셀트리온, 코로나19 항체치료제 전국 의료기관 공급 개시 2021.02.17 11:27
[속보] "재확산 땐 새 거리두기 적용 혼란…개편 후 이행시기 검토" 2021.02.17 11:23
```

