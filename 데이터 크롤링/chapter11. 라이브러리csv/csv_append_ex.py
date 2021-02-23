import csv

# 추가모드 "a"
f = open("./example.csv", "a", newline="")

wtr = csv.writer(f)

wtr.writerow(["바둑", 40, "파이썬"])
wtr.writerow(["오목", 34, "C"])

f.close()