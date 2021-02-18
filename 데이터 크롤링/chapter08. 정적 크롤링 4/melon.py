import requests
from bs4 import BeautifulSoup

while(True):
    genre = input("음악 장르 입력(발라드, 댄스, 힙합, 알앤비, 인디, 록, 트로트, 포크) : ")
    count = 0

    if genre == "발라드":
        gnrCode = "GN0100"
        break
    elif genre == "댄스":
        gnrCode = "GN0200"
        break
    elif genre == "힙합":
        gnrCode = "GN0300"
        break
    elif genre == "알앤비":
        gnrCode = "GN0400"
        break
    elif genre == "인디":
        gnrCode = "GN0500"
        break
    elif genre == "록":
        gnrCode = "GN0600"
        break
    elif genre == "트로트":
        gnrCode = "GN0700"
        break
    elif genre == "포크":
        gnrCode = "GN0800"
        break
    else:
        print("장르 입력이 잘못 되었습니다. 다시 입력해주십시오.")

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
melon_url = "https://www.melon.com/genre/song_list.htm?gnrCode=" + gnrCode
raw = requests.get(melon_url, headers = header)
soup = BeautifulSoup(raw.text, "html.parser")

box = soup.find("tbody")

all_singer = box.find_all("div", {"class":"ellipsis rank02"})
all_title = box.find_all("div", {"class":"ellipsis rank01"})

for singer, title in zip(all_singer, all_title):
    count += 1
    print(count, title.find("a").text + " - " + singer.find("a").text)