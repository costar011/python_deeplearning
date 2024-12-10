# 튜플 / 내용 변경이나 추가를 할 수 없음 속도는 리스트보다 빠름
# 변경하지 않은 목록을 활용할 때 튜플 사용함

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스") # AttributeError: 'tuple' object has no attribute 'add'
# 튜플은 내용 변경이나 추가를 할 수 없음

# name = "김종국"
# age = 20
# hobby = "코딩"
#print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)