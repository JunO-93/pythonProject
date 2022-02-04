import csv

jusik = [
    ["종목","매입가","수량","목표가"],
    ["삼성전자",85000,10,90000],
    ["NAVER",380000,5,400000]
]

# 주식 csv 파일 생성
# file = open("./mystock.csv","w",newline="",encoding='utf-8-sig')
# writer = csv.writer(file)
# for d in jusik:
#     writer.writerow(d)
# file.close()

def show_profit(data):
    name = data[0]  # 종목
    purchase_price = int(data[1])  # 매입가
    amount = int(data[2])  # 수량
    target_price = int(data[3])  # 목표가

    profit = (target_price - purchase_price) * amount
    profit_ratio = (target_price / purchase_price - 1) * 100
    print(f"{name} {profit} {profit_ratio:.2f}%")

# 주식 파일 읽기
file = open("./mystock.csv","r",encoding='utf-8-sig')
# 파일데이터 읽기
reader = list(csv.reader(file))
for data in reader[1:]:
    show_profit(data)
file.close()


# def stocksCalculater(stock,targetPrice,count,purchasePrice):
#     proceeds = (int(purchasePrice)-int(targetPrice)) * int(count) # 수익금
#     yields =  (int(purchasePrice)/int(targetPrice)-1) * 100#수익률
#     print(f"{stock} {proceeds} {round(yields,2)}%")#
#
# mystockLength = len(reader)
# #
# for i in range(1,mystockLength):
#     stocksCalculater(reader[i][0], reader[i][1], reader[i][2], reader[i][3])



