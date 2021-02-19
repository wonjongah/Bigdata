##### 라이브러리 selenium



selenium은 웹 드라이버를 사용해 자동화를 실형하는 라이브러리이다.

정적 크롤링은 HTML을 요청해 원하는 정보만 빠르게 골라냈다면, 동적 크롤링의 selenium은 사람이 데이터를 수집하는 방식 그대로 크롤링하는 기계를 만들어낸다.

정적크롤링보다 속도는 느리지만, 마우스 클릭, 키보드 입력, 뒤로가기 등의 동작이 가능해 크롤링의 한계가 없다.



##### webdriver



selenium의 webdriver는 많은 브라우저, 운영체제 및 프로그래밍 언어를 지원하며 웹 응용 프로그램들의 테스트를 단순화 및 가속화해주는 툴이다.

1. 다채로운 언어 지원
2. 쉽고 단순한 사용법
3. 실행 과정의 시각화로 인한 실시간 확인

webdriver는 사용하는 브라우저에 맞게 설치해주어야 한다.



##### chromedriver.exe



크롬 버전과 맞는 chromedriver.exe가 설치되어야 한다.



##### 라이브러리 time



time 라이브러리의 내장함수 sleep()은 동적 크롤링을 하며 많이 사용하는 함수이다.

반드시 필요하진 않으나 웹 페이지의 로딩 시간이 오래 걸릴 수도 있고, 혹시나 클릭, 입력과 같은 작업이 누락될 확률을 낮추기 위해 사용할 것을 권장한다.

이메일 내용을 크롤링한다고 생각하면, 아이디 입력 -> 비밀번호 입력 -> 메일함 클릭 -> 첫 번째 메일 클릭..

이 네 가지 작업을 아주 빠른 속도로 진행하면 웹페이지의 로딩 속도가 따라오지 못할 수 있기 때문에 time() 함수로 여유를 주면서 크롤링이 끊기지 않도록 설정해준다.



##### 동적 크롤링



```python
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
```



##### selenium 내장함수



```python
driver = webdriver.Chrome("../chromedriver")
# webdriver에 chromedriver.exe를 연결한 객체를 생성한다.
# 가상의 크롬 창을 열 수 있도록 도와주는 속성값과 행동을 driver 변수에
# driver 변수 대상으로 대부분의 내장함수를 사용한다.
```



1. get()



get() 함수는 입력한 url 주소로 접속하는 함수이다.

ex)

```python
driver.get("url 주소")
```



2. find_element_by_ ?? ()



정적크롤링의 find과 같은 역할로, 크롤링을 위해 HTML 요소를 찾는 함수이다.



-> by_css_selector

```python
driver.find_element_by_css_selector("태그 및 선택자")
```

ex)

```python
driver.find_element_by_css_selector("a#writeFormBtn")
```



-> by_id & by_class_name

id 속성 혹은 class 속성을 가지고 있는 경우 사용한다.

```python
driver.find_element_by_id("id")
driver.find_element_by_class_name("class")

ex) '글쓰기' 버튼 - <a href="#" id="writeFormBtn" class="btn_type1 post_write _rosRestrict" onclick="clickcr(this,'abt.wrtlist', '', '', event);">

driver.find_element_by_id("writeFormBtn")
driver.find_element_by_class_name("btn_type1.post_write._rosRestrict")
```

copy 목록의 copy selector를 클린해서 속성을 찾을 수 있다.



-> by_xpath

HTML 요소를 찾기 위히 적당한 id, class 속성이 없을 경우 xpath를 사용할 수 있다.

xml 문서의 특정 부분의 위치를 찾을 때 사용한다.

html 요소를 우클릭하고 copy 목록의 copy xpath를 클릭해 사용한다.

```python
driver.find_element_by_xpath('XPath 선택자')

# ex) '글쓰기' 버튼의 'Copy XPath'결과 - //*[@id="writeFormBtn"]
driver.find_element_by_xpath('//*[@id="writeFormBtn"]')
```



3. find_elements_by_?? ()



정적 크롤링의 find_all과 같은 역할로, 입력한 태그 및 선택자에 해당하는 모든 html 요소를 찾는 함수이다.

element 뒤에 s가 붙는 것에 유의해야 한다.



4. click()



html 요소를 클릭하는 함수이다.

```python
driver.find_element_by_??("태그 혹은 선택자").click()

ex) 글쓰기 버튼 클릭
driver.find_element_by_css_selector("a#writeFormBtn").click()
```



5. send_keys()



html 요소에 직접 텍스트를 입력하는 함수이다.

```python
driver.find_element_by_??().send_keys("텍스트")

ex) 검색 칸에 파이썬 입력
driver.find_element_by_css_selector("input#query").send_keys("파이썬")
```

