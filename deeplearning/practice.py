print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))

print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
print("ㅋ"*9)

# boolean 자료형
# true / false
print(5 > 10)
print(true)
print(false)
print(not true) # flase로 결과 값이 나옴
print(not false) # true로 결과 값이 나옴

print(not (5 > 10)) # true로 결과 값이 나옴

# 변수
# 애완동물을 소개해 주세요

name = "연탄이"
animal = "강아지"
age = 4
hobby = "산책"
is_adult = age >= 3


print("우리집" +animal + "의 이름은 " + name + "에요")
hobby = "공놀이"
print(name + "는" + str(age) + "살이며" + hobby +"을 아주 좋아해요")
print(name + "는 어른일깡요? " + str(is_adult)) # boolean 자료형을 str로 변환하여 출력