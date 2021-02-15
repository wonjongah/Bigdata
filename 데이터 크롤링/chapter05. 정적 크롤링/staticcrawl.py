import requests

lotto_url = "https://dhlottery.co.kr/gameResult.do?method=byWin"
raw = requests.get(lotto_url)
print(raw)
print(raw.text)