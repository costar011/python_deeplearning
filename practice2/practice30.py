# class

# 마린 : 공격 유닛, 군인, 총을 쏠 수 있음


# name = "마린" # 유닛의 이름
# hp = 40 # 유닛의 체력
# damage = 5 # 유닛의 공격력

# print("{0} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# 탱크 : 공격 유닛, 탱크, 포를 쏠 수 있는데, 일반 모드 / 시즈 모드

# thak_name = "탱크"
# thank_hp = 150
# thak_damage = 35

# print("{0} 유닛이 생성되었습니다.".format(thak_name))
# print("체력 {0}, 공격력 {1}\n".format(thank_hp, thak_damage))

# thak2_name = "탱크"
# thank2_hp = 150
# thak2_damage = 35

# print("{0} 유닛이 생성되었습니다.".format(thak2_name))
# print("체력 {0}, 공격력 {1}\n".format(thank2_hp, thak2_damage))


# def attack(name, location, damage):
#    print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(name, location, damage))

# attack(name, "1시", damage)
# attack(thak_name, "1시", thak_damage)
# attack(thak2_name, "1시", thak_damage)

# 클래스는 붕어빵 틀과 같다. 붕어빵 틀로 찍어내면 붕어빵이 나오듯이 클래스로 만들어낸 것을 객체라고 한다.


class Unit:
    def __init__(self, name, hp, damage):  # __init__ : 파이썬에서 쓰이는 생성자
        self.name = name  # 멤버 변수
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)  # 객체
marine2 = Unit("마린", 40, 5)  # 객체

thak = Unit("탱크", 150, 35)  # 객체