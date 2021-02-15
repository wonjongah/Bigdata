1. 크롤링을 할 웹 사이트 선정
2. 데이터 선정



##### 크롤링 대상 사이트 살펴보기



정적, 동적 크롤링 중 어떤 것이 더 적합할 지 생각해야 한다.

로또 당첨 번호를 크롤링하고 싶을 때 HTML을 통해 구조를 파악해야 한다.

https://dhlottery.co.kr/gameResult.do?method=byWin

```html
<div class="nums">
		<div>
				<strong> </strong>
				<p>
					<span> </span>
					<span> </span>
					<span> </span>
					<span> </span>
					<span> </span>
					<span> </span>
				</p>
		</div>
		<div>
				<strong> </strong>
				<p>
					<span> </span>
				</p>
		</div>
</div>
```

\<div class="num"> 안의 \<span> 태그만 뽑아내면 당첨번호를 수집할 수 있다.

1. 웹 사이트의 주소에 접속하면 한 페이지 내에 원하는 데이터가 모두 있는가
2. 원하는 데이터의 태그를 살펴본 결과 클릭, 입력, 페이지 이동의 변화가 없어도 데이터 수집이 가능한가



##### 라이브러리 requests



requests 라이브러리는 파이썬에서 HTTP와 관련된 작업을 편하게 해주는 라이브러리이다.

웹 페이지에 무언가의 작업 요청을 할 수 있는 클래스이다.



##### 웹 사이트의 HTML 불러오기



requests 라이브러리를 사용하는 이유는 웹 사이트의 HTML 코드를 불러오기 위함이다.

원하는 정보를 빼오기 위해선 먼저 HTML 코드 전체를 불러와야 한다.



- get() 함수



requests 라이브러리의 get() 함수는 웹 페이지의 내용을 요청하는 함수이다.

```python
requests.get("url 주소")
```



##### 파이썬 코드 작성



```python
import requests

lotto_url = "https://dhlottery.co.kr/gameResult.do?method=byWin"
raw = requests.get(lotto_url)
print(raw)
```

```
<Response [200]>
```

Response [200]이 출력됐다면 get() 함수를 통해 보낸 요청에 응답이 제대로 이루어졌다는 뜻이다.

결과를 확인하고 싶다면 

```python
print(raw.text) # text 형식으로 출력하라
```

코드를 더하면 된다.

```python
import requests

lotto_url = "https://dhlottery.co.kr/gameResult.do?method=byWin"
raw = requests.get(lotto_url)
print(raw)
print(raw.text)
```

```
<Response [200]>

<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="EUC-KR">
<meta id="utitle" name="title" content="동행복권">
<meta id="desc" name="description" content="동행복권 950회 당첨번호 3,4,15,22,28,40+10. 1등 총 8명, 1인당 당 
첨금액 3,281,920,500원.">
<title>로또6/45 - 회차별 당첨번호</title>
<title>동행복권</title>

<meta http-equiv="X-UA-Compatible" content="IE=edge">
<link rel="shortcut icon" href="/images/common/favicon.ico" type="image/x-icon">
<link rel="icon" href="/images/common/favicon.ico" type="image/x-icon">
<script type="text/javascript" src="/js/jquery-1.9.1.min.js"></script>
<script type="text/javascript" src="/js/jquery-ui.js"></script>
<script type="text/javascript" src="/js/common.js" charset="utf-8"></script>
<script type="text/javascript">

fn_g_init_message("");

var gameUserId = "";

.............


function check_if_Valid_top() {
        var f = document.frmLogin;

        if (f.userId.value == "") {
                alert("아이디를 입력해 주십시오");
                f.userId.focus();
                return;
        }
        if (f.password.value == "") {
                alert("비밀번호를 입력해 주세요");
```

