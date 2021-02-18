import requests
from bs4 import BeautifulSoup

keyword = input("뉴스 검색 키워드 : ")
count = 0

for page in range(1, 11):
    news_url = "https://search.hankyung.com/apps.frm/search.news?query=" + keyword + "&page=" + str(page)
    raw = requests.get(news_url)

    soup = BeautifulSoup(raw.text, "html.parser")

    box = soup.find("ul", {"class":"article"})
    all_title = box.find_all("em", {"class":"tit"})

    for title in all_title:
        count += 1
        print(count, "-", title.text.strip())
    print()