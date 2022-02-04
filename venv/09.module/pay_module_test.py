import datetime
import pay_module

# 변수사용
print(pay_module.version)

# 함수사용
pay_module.printAuthor()

# 클래스사용
pay_info = pay_module.Pay("A1203",13000,datetime.datetime.now())
print(pay_info.get_pay_info())


# 모듈 밖에서 실행하면 모듈이름이 나옴
print(pay_module.__name__)

