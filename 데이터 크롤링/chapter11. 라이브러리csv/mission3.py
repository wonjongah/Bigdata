import csv

f = open("./covid19_articles.csv", "r", newline="")

rdr = csv.reader(f)
next(rdr)

# 속보 기사 개수
count = 0

for r in rdr:
    # 기사 제목에 [속보]가 포함되어 있다면 프린트 + 개수 추가
    if "[속보]" in r[2]:
        count += 1
        print(r[2])
print(f"속보 기사 개수 : {count}")

f.close()