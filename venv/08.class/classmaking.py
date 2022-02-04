# 파이썬에서는 자료형도 클래스다!

a = 10
b = "문자열객체"
c = True


class Monster:
    def __init__(self,health,attack,speed):
        self.health = health
        self.attack = attack
        self.speed = speed
    def decrease_health(self,num):
        self.health -= num
    def get_health(self):
        return(self.health)

# 고블린 인스턴스 생성
goblin = Monster(800,120,300)
goblin.decrease_health(100)
print(goblin.get_health())

# 울프 인스턴스 생성
wolf = Monster(1500,200,350)
wolf.decrease_health((1000))
print(wolf.get_health())


