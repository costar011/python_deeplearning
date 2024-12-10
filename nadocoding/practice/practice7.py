# 문자열 처리 함수

python = "Python is Amazing"
print(python.lower()) # 모든 문자를 소문자로 변환
print(python.upper()) # 모든 문자를 대문자로 변환
print(python[0].isupper()) # 첫번째 문자가 대문자인지 확인
print(len(python)) # 문자열 길이 출력
print(python.replace("Python", "Java")) # 문자열 대체

index = python.index("n") # 문자열에서 n이 몇 번째에 있는지 확인
print(index)

index = python.index("n", index + 1) # 문자열에서 n이 몇 번째에 있는지 확인
print(index)

print(python.find("Java")) # 문자열에 해당 문자열이 없으면 -1 반환
# print(python.index("Java")) # 문자열에 해당 문자열이 없으면 오류 발생 / python 변수에는 Java가 없음
# find와 index의 차이점은 find는 해당 문자열이 없으면 -1을 반환하고, index는 해당 문자열이 없으면 오류 발생

print(python.count("n")) # 문자열에서 n이 총 몇번 등장하는지 확인