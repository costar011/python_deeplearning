# 사전(Dictionary) / key는 중복이 안됨

# cabinet = {3: "유재석", 100: "김태호"} # key는 3, 100 / value는 유재석, 김태호
# print(cabinet[3]) # 유재석
# print(cabinet[100]) # 김태호

# print(cabinet.get(3)) # 유재석
# print(cabinet[5]) # KeyError: 5

# print(cabinet.get(5)) # None
# print(cabinet.get(5, "사용 가능")) # 사용 가능
# print("hi")

# print(3 in cabinet) # True # 3이 cabinet에 있나?
# print(5 in cabinet) # False # 5가 cabinet에 있나?

cabinet = {"A-3": "유재석", "B-100": "김태호"}
print(cabinet["A-3"]) # 유재석
print(cabinet["B-100"]) # 김태호

# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국" # 유재석 -> 김종국
cabinet["C-20"] = "조세호"
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

# key들만 출력
print(cabinet.keys())

# value들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)