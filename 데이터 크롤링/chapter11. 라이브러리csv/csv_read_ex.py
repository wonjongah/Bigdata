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