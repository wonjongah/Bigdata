##### 라이브러리



크롤링을 사용하기 위해서 라이브러리를 사용해야 한다.

라이브러리는 프로그래밍을 할 때 더 다양한 기능을 사용할 수 있도록 유용한 프로그램들을 모아놓은 것이다.

라이브러리 사용 코드는 다음과 같다.

```python
import 라이브러리 # 해당 라이브러리 전체를 가져온다.
from 라이브러리 import 메소드 # 해당 라이브러리의 특정 메소드를 가져온다.
```



##### time 라이브러리



```python
import time
```



- time.time()



time.time()은 UTC를 사용해 현재 시간을 실수 형태로 돌려주는 함수이다.

1970년 1월 1일 0시 0분 0초 기준으로 지난 시간을 초 단위로 돌려준다.

```python
import time

print(time.time())
```



- time.localtime()



현재 시간을 년, 월, 일, 시, 분, 초..의 형태로 출력해준다.

```python
import time

print(time.localtime())
```



##### 정적 클로링 도구



- requests



간편한 HTTP 요청 처리를 위해 사용하는 라이브러리로, 웹과 연결을 위해 사용된다.



- beautifulsoup



html 태그를 다룰 수 있는 라이브러리로, 웹에 있는 데이터 중 필요한 데이터만 뽑아내기 위해 사용한다.



##### 독적 크롤링 도구



- selenium



웹 드라이버를 사용해 자동화 기능을 실현하는 라이브러리이다.

웹에 접속해 클릭, 이동과 같으 제어를 하는데 사용한다.



- chromedriver.exe



나의 크롬의 버전과 맞는 chromedriver.exe를 소스코드와 같은 경로에 다운로드하기.