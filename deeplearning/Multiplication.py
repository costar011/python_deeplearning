# 산술연산 #
3.14 * 10 * 10 # 314.0 #
3.14 * 10 ** 2 # 314.0 #


# 자료형 #
type(10) # int #
type(3.14) # float #
type("python") # str #


# 변수 #
r = 20
pi = 3.14 # 원주율 정의 #
area = pi * r ** 2
area    # 1256.0 #

# 리스트 #
lst = [10, 20, 30, 40, 50]      # 리스트 정의 #
lst # [10, 20, 30, 40, 50] #    # 리스트 출력 #

lst[2]                          # 리스트의 요소 접근 #
# 30 #

lst[2] = 90                     # 3번쨰 요소를 90으로 변경 #
lst                             # 리스트 출력 #
# [10, 20, 90, 40, 50] #

len(lst)                        # 리스트의 길이 #
# 5 #

## 리스트에는 슬라이싱을 사용할 수 있다  ##
## 슬라이싱은 리스트의 일부분을 가져오는 것이다 ##

lst[0:3]                        # index 0부터 2까지 추출 #
# [10, 20, 90] #

# 1부터 10까지 수 세기 #
for i in range(1, 11):
    print(i, end=" ")                    # 1부터 10까지 출력 #

# 1부터 100까지 수 중 짝수만 세기 #
for i in range(1, 101):
    if i % 2 == 0:
        print(i, end=" ")                # 짝수만 출력 #

# 1부터 100까지 수 중 3의 배수만 세기 #
for i in range(1, 101):
    if i % 3 == 0:
        print(i, end=" ")                # 3의 배수만 출력 #

# 1부터 100까지 수 중 3의 배수이면서 5의 배수인 수 세기 #
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i, end=" ")                # 3의 배수이면서 5의 배수인 수 출력 #

# 입력된 수가 짝수인지 확인 #
num = int(input("숫자를 입력하세요: ")) # 입력된 수를 정수로 변환 #
if num % 2 == 0:
    print("짝수입니다.")                # 짝수인 경우 출력 #
else:
    print("홀수입니다.")                # 홀수인 경우 출력 #


# 입력된 수가 3의 배수인지 확인 #
num = int(input("숫자를 입력하세요: ")) # 입력된 수를 정수로 변환 #
if num % 3 == 0:
    print("3의 배수입니다.")           # 3의 배수인 경우 출력 # 
else:
    print("3의 배수가 아닙니다.")       # 3의 배수가 아닌 경우 출력 #   


a = 50
b = 40

result = a / b
print(result)

result = a // b # 나눴을 때 몫
print(result)

result = a % b # 나누었을 때 나머지
print(result)

name = 'mike'
print(name)

city = 'seoul'
print(city)

a = 10.5
print(a)
