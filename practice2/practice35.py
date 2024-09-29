# pass / super() : 부모 클래스의 생성자를 호출할 때 사용

# 일반 유닛
class Unit:
    def __init__(self, name, hp, damage):  # __init__ : 파이썬에서 쓰이는 생성자
        self.name = name  # 멤버 변수
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

# 공격 유닛
class AttackUnit(Unit):  # 상속
    def __init__(self, name, hp, speed, damage):  # __init__ : 파이썬에서 쓰이는 생성자
        Unit.__init__(self, name, hp, damage, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 드랍쉽 : 공중 유닛, 수송기. 마린/ 파이어뱃/ 탱크 등을 수송. 공격 X -> 공격 유닛 클래스를 상속받지 않음
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):  # 다중 상속
    def __init__(self, name, hp, damage, flying_speed):  
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)


# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # 어떤 class를 상속받아서 초기화를 할 때 그 class를 적고 __init__을 적어준다. 
        # pass 아무것도 안하고 넘어가겠다.
        # Unit.__init__(self, name, hp, 0)  # 건물은 이동 불가
        super().__init__(name, hp, 0)  # super를 통해서 초기화를 할 때는 self 정보는 안보내줘야한다
        self.location = location

# 서플라이 디폿 : 건물, 1개 건물 = 8개 유닛.
#supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

# def game_start():
#    print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#    pass # 아무것도 안하고 넘어가겠다.

# game_start()
# game_over()
