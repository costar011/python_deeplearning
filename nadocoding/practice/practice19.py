# for문

# 출석번호가 1, 2, 3, 4 앞에 100을 붙이기로 함 -> 101, 102, 103, 104

# students = [1, 2, 3, 4, 5]
# print(students)

# students = [i+100 for i in students] # i에다가 100을 더한 값을 리스트에 넣겠다
# print(students)

# 학생 이름을 길이로 변환
students = ["Iron man","thor","groot"]
students = [len(i) for i in students] # len 함수는 문자열의 길이를 반환
print(students)

# 학생 이름을 대문자로 변환
students = ["Iron man","thor","groot"]
students = [i.upper() for i in students] # upper 함수는 대문자로 변환
print(students)