import csv

data = [
    ["이름","반","번호"],
    ["재석",1,20],
    ["홍철",3,8],
    ["형돈",5,38]
]

file = open("./student.csv","w", newline="", encoding="utf-8-sig")
writer = csv.writer(file)

for d in data:
    writer.writerow(d) # 리스트로 저장된 데이터가 csv 파일에 한줄씩 저장됨

file.close()
