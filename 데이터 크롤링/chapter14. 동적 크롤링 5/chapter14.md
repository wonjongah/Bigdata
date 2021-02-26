그동안 동적 크롤링은 한 탭에서 모든 화면 전환이 이루어졌다.

클릭 시 크롬 창에 새로운 탭이 생길 때 직접 탭을 다루는 소스코드를 작성해주어야 한다.

```python
driver.window_handles
```

driver.window_handles는 크롬 창에서 열린 탭을 모두 담고 있다.

ex)

```python
driver.window_handles # 열린 탭 목록
len(driver.window_handles) # 열린 탭 개수
driver.window_handles[0] # 첫 번째 탭
driver.window_handles[1] # 두 번째 탭
driver.window_handles[-1] # 마지막에 열린 탭, 가장 오른쪽 탭
# 리스트와 같이 사용하면 된다.
```



```python
driver.switch_to.window(작업할 탭)
```

여러 개의 탭이 켜지면 driver 변수도 바꿔줘야 한다.

기존의 driver는 이전 탭의 driver고, 새로 켜진 탭에서 작업을 해야 한다면 driver 변수를 새로 켜진 탭으로 전환해줘야 한다. 

이때 driver.switch_to.window()를 사용한다.

ex)

```python
# 1. 새로운 탭 켜짐

# 2. driver 변수를 새로운 탭으로 전환
driver.switch_to.window(driver.window_handles[-1])

# 3. 새로운 탭에서 작업
클릭, 갑 입력, 내용 수집 등의 작업 수행

# 4. 작업을 마치면 새로운 탭을 닫음
driver.close()

# 5. 다시 처음 탭으로 전환
driver.switch_to.window(driver.window_handles[0])
```

