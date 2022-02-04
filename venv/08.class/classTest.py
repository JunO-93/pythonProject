#클래스 실습 문제

class Item():
    def __init__(self,name,price,weight,isdropable):
        self.name = name
        self.price = price
        self.weight = weight
        self.isdropable = isdropable
    def sale(self):
        print(f"[{self.name}]의 가격은 {self.price} 입니다")
    def discard(self):
        if self.isdropable:
            print(f"[{self.name}]을 버렸습니다.")
        else:
            print(f"[{self.name}]는 버릴 수 없는 아이템입니다.")

class WearableItem(Item):
    def __init__(self,name,price,weight,isdropable,effect):
        super().__init__(name,price,weight,isdropable)
        self.effect = effect
    def wear(self):
        print(f"[{self.name}]를 착용하여 {self.effect}의 효과가 적용되었습니다.")

class UsableItem(Item):
    def __init__(self,name,price,weight,isdropable,effect):
        super().__init__(name,price,weight,isdropable)
        self.effect = effect
    def use(self):
        print(f"[{self.name}]를 사용하여 {self.effect} 하였습니다. ")

armor = WearableItem("갑옷",50000,0.1,False,"방어력+10")
armor.sale()
armor.discard()
armor.wear()

gloves = WearableItem("장갑",100000,0.1,True,"크리티컬데미지+8")
gloves.sale()
gloves.discard()
gloves.wear()

hpPotion= UsableItem("HP포션",1000,0.01,True,"HP이(가) 500증가")
hpPotion.sale()
hpPotion.discard()
hpPotion.use()

mpPotion= UsableItem("MP포션",1000,0.01,True,"MP이(가) 500증가")
mpPotion.sale()
mpPotion.discard()
mpPotion.use()