##### 선택자



태그 중에는 동일한 태그가 존재할 것이다.

선택자(Selector)는 동일한 태그 여러 개 중에서도 각 태그를 구별할 수 있는 일종의 주소라고 할 수 있다.



##### 선택자의 필요성



```html
<div>	
	<div>
		<span> 파이썬 </span>
		<span> 크롤링 </span>
	</div>
	
	<div>
		<span> C언어 </span>
		<span> 게임 </span>
	</div>
<div>
```

같은 태그의 반복으로 컴퓨터는 특정 태그에 대해서 혼돈이 올 수 있다.

예를 들어 글자를 감싸는 <span> 태그는 다양한 내용을 담을 수 있다.

그러나 <span> 태그가 4개나 있어서 컴퓨터가 구분하기 어렵다.

이러한 문제를 해결하기 위해 선택자를 사용해야 한다.

```html
<div id = "contents">	
	<div class = "metadata1">
		<span class = "language"> 파이썬 </span>
		<span class = "project" > 크롤링 </span>
	</div>
	
	<div class = "metadata2">
		<span class = "language"> c언어 </span>
		<span class = "project"> 게임 </span>
	</div>
<div>
```

언어(language)와 관련된 데이터만 필요하다면, 태그로만 해당 데이터를 선택하면, <span>을 사용할 것이다.

하지만 <span>에 언어 정보 뿐만 아니라 프로젝트 정보(크롤링, 게임)도 포함됩니다.

이러한 경우, 원하는 정보만 찾는 것이 힘들지만 "class = 'language'"라는 선택자를 통해 우리는 두 개의 언어 관련 데이터(파이썬, C언어)를 찾을 수 있다.



##### id와 class



태그의 선택자는 주로 id와 class를 사용한다.

id는 어떤 요소의 고유한 값을 말한다.

html에서도 id는 하나의 고유한 선택자로, 중복되지 않고 하나만 존재한다.

class 태그는 같은 속성을 지닌 데이터를 묶어주는 값이다. 한 태그가 여러 개의 class를 가질 수 있다.

비슷한 속성끼리 묶어줄 때 class 태그를 사용한다.



##### 선택자 사용법



```html
<div id='123' class='456'>
```

선택자에 따라 데이터를 찾는 코드에 차이가 있다.

id는 '#'를 붙이고, class는 '.'을 붙여준다.

- 태그만 사용해 데이터를 찾을 경우 -> 태그
  - div
- 태그와 id를 사용해 데이터를 찾을 경우 -> 태그#id
  - div#123
- 태그와 class를 사용해 데이터를 찾을 경우 -> 태그.class
  - div.456
- 태그, id, class 모두 사용해 데이터를 찾을 경우 -> 태그#id.class
  - div#123.456



class 이름에 공백이 포함될 경우가 종종 있는데, 이럴 경우 공백을 .으로 대체해서 작성하면 된다.

ex)

```html
<div class='hello python'>
```

-> div.hello.python



##### 선택자 실습



#12를 통해 검색 후 ctrl + F를 통해 검색 가능하다.

위에서 배웠던, .과 #을 사용해 찾고 싶은 결과 검색이 가능하다.

예를 들어 id="article"인 div 태그 안의 class="nums"인 div 태그가 찾고 싶다면,

```html
div#article div.nums
```

검색을 통해 찾을 수 있다.

```
id : #
class : .
```

```
id 선택자 + class 선택자
```

식으로 더 정확한 데이터를 검색할 수 있다.