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