# 상속
# 부모클래스

# 클래스 변수
# : 인스턴스들이 모두 공유하는 변수

import random

class Monster():
    max_num = 1000
    def __init__(self,name,health,attack):
        self.name = name
        self.health = health
        self.attack = attack
        Monster.max_num -=1
    def move(self):
        print(f"[{self.name}] 지상에서 이동하기")

# 자식 클래스
class Wolf(Monster):
    pass

class Shark(Monster):
    def move(self): #메서드 오버라이딩 : 메서드 재정의
        print(f"[{self.name}] 헤엄치기")

class Dragon(Monster):
    #생성자 오버라이딩
    def __init__(self,name,health,attack,skills):
        super().__init__(name,health,attack) # 부모클래스의 생성자 불러옴
        self.skills=skills #새로 추가된 것만 추가
    def move(self):
        print(f"[{self.name}] 날기")
    def skill(self):
        print(f"[{self.name}] 스킬사용 {self.skills[random.randint(0,2)]}")

wolf = Wolf("울프",1500,200)
wolf.move()
print(wolf.max_num)

shark = Shark("상어",2000,300)
shark.move()
print(shark.max_num)

dragon = Dragon("드래곤",8000,800,("파괴광선","꼬리치기",'용의숨결'))
dragon.move()
dragon.skill()
print(shark.max_num)