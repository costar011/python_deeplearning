# 변수
# 애완동물을 소개해 주세요

name = "연탄이"
animal = "강아지"
age = 4
hobby = "산책"
is_adult = age >= 3


print("우리집" +animal + "의 이름은 " + name + "에요")
hobby = "공놀이"

# print(name + "는" + str(age) + "살이며" + hobby +"을 아주 좋아해요")
print(name , "는" + age + "살이며 ," + , hobby,  +"을 아주 좋아해요") # + 대신 ,를 사용하여 출력 / 이때는 int나 boolean 형식을 str로 변환하지 않아도 출력 가능 / ,를 사용하면 띄어쓰기가 자동으로 됨
print(name + "는 어른일깡요? " + str(is_adult)) # boolean 자료형을 str로 변환하여 출력
