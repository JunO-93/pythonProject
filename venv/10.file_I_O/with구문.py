# with 구문을 사용하면 자동으로 file cloase 해준다
with open("./data.txt", "r", encoding="utf8") as file:
    data = file.read()
    print(data)