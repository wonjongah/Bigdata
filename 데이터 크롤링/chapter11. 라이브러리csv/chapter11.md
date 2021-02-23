#### csv 파일



csv는 Comma separated Values의 약어로, 콤마(',')로 구분된다는 뜻이다.

즉, csv 파일은 콤마로 구분된 텍스트 데이터 혹은 텍스트 파일을 뜻한다.

확장자는 .csv이다.

한 줄이 하나의 행이 되며, 콤마를 기준으로 열을 구분한다.

ex) 이름,나이,언어

​		길동,10,파이썬

| 이름 | 나이 | 언어   |
| ---- | ---- | ------ |
| 길동 | 10   | 파이썬 |



#### csv 파일 사용 이유



많은 양의 데이터를 다룰 때 모든 서식은 제거되고 데이터 값만 저장되므로 필요한 데이터만 남겨 데이터의 무게를 줄일 수 있다.

다른 소프트웨어로 데이터를 쉽게 이전도 가능하다.



#### 파이썬의 csv 라이브러리



```python
import csv
```

의 형태로 임포트해 사용한다.

파이썬으로 csv 파일을 작성할 때는 행 단위로 작성한다는 점을 기억해야 한다.

writer, reader 두 객체를 사용해 csv 파일을 작성하고 읽을 수 있다.

파일을 닫는 코드까지 작성한 후 소스코드 실행을 권장한다. 파일을 닫는 코드 없이 계속 실행하면 파일이 겹치면서 에러가 발생할 수 있다.



```python
# writerow() 기본 코드
wtr.writerow([값1, 값2, 값3, ...])
```



ex) writer 

```python
import csv

# 작성할 example.csv 파일을 생성해 f에 저장
# newline 옵션으로 한 줄씩 건너 뛰는 현상 해결
f = open("./example.csv", "w", newline= "")

# csv 파일을 작성하는 객체 변수 wtr 생성
wtr = csv.writer(f)

# 열 제목 작성
wtr.writerow(["이름", "나이", "언어"])

# 데이터 생성
all_name = ["길동", "철수", "영희"]
all_age = [10, 20, 30]
all_language = ["파이썬", "C", "자바"]

# 각 행에 데이터 작성
for i in range(3):
    name = all_name[i]
    age = all_age[i]
    language = all_language[i]
    wtr.writerow([name, age, language])

f.close()
```



ex) reader 

```python
import csv

# 일거올 example.csv 파일을 변수 f에 저장
f = open("./example.csv", "r")

# csv 파일의 모든 데이터 변수를 rdr에 저장
rdr = csv.reader(f)

# rdr의 첫 번째는 건너뜀(열 제목)
next(rdr)

# 이중리스트 형태로 되어 있는 rdr을 한 요소씩 출력
for row in rdr:
    print(row)

f.close()
```



ex) append

```python
import csv

# 추가모드 "a"
f = open("./example.csv", "a", newline="")

wtr = csv.writer(f)

wtr.writerow(["바둑", 40, "파이썬"])
wtr.writerow(["오목", 34, "C"])

f.close()
```

