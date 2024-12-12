'''
실습 1 / 평가프로그램
Input()으로 score 변수에 값을 넣고 age 변수에 나이 값을 넣은 후 프로그램 실행 시
점수가 100인 경우 "Perfact!!!" 출력 , 70인 경우 "Good" 출력 , 50점 이하 "Not Good" 출력
그 외 Not Bad
단, 나이가 60 이상일 시 가점 10점 추가
'''

age = int(input("your Age > "))
score = int(input("your Score > "))

def score2(scorenum):
    if scorenum >= 100:
        return "Perfact!!"
    elif scorenum <= 100 and scorenum >= 70:
        return "Good"
    elif scorenum <= 50:
        return "Not Good"
    else:
        return "Not Bad"


if age >= 60:
    score += 10
    print(score2(score))
else:
    print(score2(score))