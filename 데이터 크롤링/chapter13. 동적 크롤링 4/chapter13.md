자동입력방지를 피하기 위해서 send_keys() 대신 execute_script() 함수를 사용한다.



크롤링을 하다보면 원하는 정보가 화면에 보이고, html 코드에서도 원하는 정보가 모두 나타나지만, 파이썬으로 찾아보면 없거나 크롤링되지 않을 때 프레임으로 만들어진 부분이 있나 확인해야 한다.

프레임은 웹페이지의 html 안에 또 다른 html을 넣어둔 것이라고 생각하면 쉽다.

프레임을 확인하기 위해선 html 코드를 확인해야 한다.

F12에 ctrl + f를 통해 iframe을 검색한다.

홈페이지 안에 또 다른 큰 창을 발견할 수 있다.

https://cafe.naver.com/codeuniv 카페의 경우 <iframe name="cafe_main" id="cafe_main" title="카페 메인" src="//cafe.naver.com/MyCafeIntro.nhn?clubid=30026525" width="860" height="100%" frameborder="0" scrolling="no" marginwidth="0" marginheight="0" allowtransparency="true" allowfullscreen="" style="height: 1891px;"></iframe>

여기서 프레임의 name을 사용해 크롤링할 때 프레임을 전환해준다.

```python
driver.switch_to.frame("프레임의 name")
```

