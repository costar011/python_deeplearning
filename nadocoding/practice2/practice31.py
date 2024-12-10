# _init_


# _init_ 은 생성자이다. 객체가 생성될 때 자동으로 호출되는 부분이다.
class Unit:
    def __init__(self, name, hp, damage):  # __init__ : 파이썬에서 쓰이는 생성자
        self.name = name  # 멤버 변수
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# 멤버 변수
# 멤버 변수는 클래스 내에서 정의된 변수이다. self.name, self.hp, self.damage 가 멤버 변수이다.

# 레이스 : 공중 유닛, 비행기, 클로킹(상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage)) # wraith1. 으로 접근하여 멤버 변수에 접근할 수 있다. 

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True  # 외부에서 멤버 변수를 확장할 수 있다.

if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))  # wraith2. 으로 접근하여 멤버 변수에 접근할 수 있다.