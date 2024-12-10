# 연산자
print(1+1) # 2
print(3-2) # 1
print(5*2) # 10

# 수식
print(2 + 3 * 4) # 14
print((2 + 3) * 4) # 20

number = 2 + 3 * 4 # 14
print(number)

number = number + 2 # 16
print(number)

number += 2 # 18
print(number)

# 숫자 처리 함수
# abs : 절대값
print(abs(-5)) # 5 절대값

# pow : 제곱
print(pow(4, 2)) # 4^2 = 4*4 = 16

# max : 최대값
print(max(5, 12)) # 12

# min : 최소값
print(min(5, 12)) # 5

# round : 반올림
print(round(3.14)) # 3

# round : 반올림
print(round(4.99)) # 5

# math 라이브러리 사용
from math import * # math 라이브러리에 있는 모든 것을 사용하겠다는 의미

print(floor(4.99)) # 내림 , 4
print(ceil(3.14)) # 올림 , 4
print(sqrt(16)) # 제곱근 , 4
