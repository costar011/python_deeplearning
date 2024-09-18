# 기본값

# def profile(name, age, main_lang):
#     print("이름: {0}\t나이: {1}\t주 사용 언어: {2}"\
#        .format(name, age, main_lang))
#  \를 사용하면 줄바꿈을 하지 않고 이어서 쓸 수 있다

profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")

# 같은 학교, 같은 학년, 같은 반, 같은 
def profile(name, age=17, main_lang="파이썬"):
    print("이름: {0}\t나이: {1}\t주 사용 언어: {2}"\
       .format(name, age, main_lang)) # \를 사용하면 줄바꿈을 하지 않고 이어서 쓸 수 있다

profile("유재석")
profile("김태호")


# 키워드 값

def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name="유재석", main_lang="파이썬", age=20)
profile(main_lang="자바", age=25, name="김태호")

# 키워드 값은 순서가 달라도 상관없다
# 매개변수에 값을 넣을 때 순서를 지키지 않아도 됨