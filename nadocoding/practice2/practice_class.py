# super

class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable): # 다중 상속
    def __init__(self):
        # super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)

# 드랍쉽
dropship = FlyableUnit()  # 두 클래스를 상속받은 클래스의 생성자는 먼저 상속받은 클래스의 생성자를 호출한다.