##### 라이브러리 BeautifulSoup



BeautifulSoup 라이브러리는 HTML 문설르 탐색해서 원하는 부분만 쉽게 뽑아낼 수 있게 해주는 라이브러리이다.



##### BeutifulSoup의 필요성



'requests'만으로도 HTML 코드를 불러왔는데 어째서 BeautifulSoup이 필요할까?

<u>raw.text로 HTML 코드를 확인했지만, HTML 코드 자체를 출력한 것이 아니다.</u>

<u>그저 HTML을 텍스트 형태(문자열 타입)로 출력했을 뿐이다.</u>

크롤링을 위해선 단순히 문자열을 다루는 것이 아니라, 실제 HTML 코드를 다뤄야 한다.

<u>BeautifulSoup 라이브러리는 위의 텍스트 결과를 실제 HTML 코드로 변환해준다.</u>



##### BeautifulSoup



- 함수 BeautifulSoup()



문자열 HTML 코드를 실제 HTML 코드로 변환해주는 함수가 바로 BeautifulSoup이다.

```python
BeautifulSoup(문자열, 'html.parser')
# 문자열을 HTML 코드로 해석해서 읽어라
```



- 함수 find_all()



find_all() 함수는 HTML 코드에서 우리가 원하는 부분을 모두 가져오는 함수이다.

원하는 부분을 지정할 때 사용하는 것은 태그와 선택자이며, find_all()은 해당 태그의 모든 HTML 코드를 리스트 형태로 반환해준다.

```python
# <div id="example1">
실제HTML코드.find_all("div") # 태그 이름
실제HTML코드.find_all(id="example1") # 선택자 정보

# <div id="example1">, <span class="example2">
실제HTML코드.find_all(["div", "span"]) # 태그 이름
실제HTML코드.find_all(attrs = {"id":"example1", "class":"example2"}) # 선택자 정보
```



- 함수 find()



find() 함수는 딱 하나만 가져온다.

```python
# <div id="example1">
실제HTML코드.find("div") # 태그 이름
실제HTML코드.find(id="example1") # 선택자 정보
실제HTML코드.find(attrs = {"id":"example1"}) # 선택자 정보
실제HTML코드.find("div", {"id":"example1"}) # 태그 이름 + 선택자 정보
```



- 함수 find() vs find_all()



크롤링을 효율적으로 수행하기 위해서 경우에 따라 두 함수를 적절히 사용해야 한다.



ex)

```python
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
```

```
< 최근 로또 당첨 번호 >
3
4
15
22
28
40
10
```

