import csv

f = open('./covid19_articles.csv', 'r')

lines = csv.DictReader(f)

for line in lines:
    if line['뉴스기사제목'].find('[속보]') != -1:
        print(line['뉴스기사제목'])