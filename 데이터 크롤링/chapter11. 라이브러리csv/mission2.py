import csv

f = open("./covid19_articles.csv", "r", newline="")

rdr = csv.reader(f)
next(rdr)

# 속보 기사 개수
count = 0

for r in rdr:
    # 기사 제목의 세 번째까지의 글자가 [속보]면 프린트 + 개수 추가
    if r[2][:4] == "[속보]":
        count += 1
        print(r[2])
print(f"속보 기사 개수 : {count}")

f.close()