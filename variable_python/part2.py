# 참 거짓을 나타내는 변수도 있다.
live_in_seoul = True
print(live_in_seoul)

live_in_tokyo = False
print(live_in_tokyo)

# List (리스트)
# 많은 데이터를 한꺼번에 다루려면 리스트를 사용한다.
names = ['mike', 'jane', 'tom']
print(names)

print(names[0])  # 리스트의 첫번째 값을 가져옵니다. 컴퓨터는 항상 0부터 시작한다.

print(names[1])
print(names[2])
# print(names[3]) # 에러가 생깁니다. 리스트의 길이보다 큰 인덱스에 접근하려고해서 그렇다.

# 리스트에 있는 값에 접근하려면 인덱스를 써야된다.
# 인덱스는 names[0]에서 [0] 같은 걸 말하는데, 항상 0부터 시작하고, 리스트의 길이보다 작아야한다.
