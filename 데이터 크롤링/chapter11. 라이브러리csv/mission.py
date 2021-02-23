import csv

f = open("./covid19_articles.csv", "r", newline="")

rdr = csv.reader(f)
next(rdr)

# 속보 기사 저장 리스트
breaking_news = []

for r in rdr:
    # 기사 제목이 [속보]로 시작된다면 breaking_news 리스트에 append
    if r[2].startswith("[속보]"):
        # 속보를 나중에 쓸 일이 있으면 새 리스트에 저장했다가 출력
        # 아니라면 바로 count로 개수 세고 출력해도 무관할 듯
        breaking_news.append(r[2])
        # 굳이 반복문 한 번 더 돌려서 breaking_news 출력하지 말고 바로 출력
        # print(r[2])
        print(breaking_news[-1])
print(f"속보 기사 개수 : {len(breaking_news)}")

f.close()