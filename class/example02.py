'''
실습 2 / 숫자 분류 프로그램
Input()으로 number 변수에 값을 넣고 소수점수(float), 정수(Integer), 자연수(natural), 짝수(even), 홀수(odd) 출력
ex) 3.45 > 'float number'
3 > 'integer number' 'natural number' 'odd number'
-3 > 'integer number'
'''

number = float(input("your want number > "))

if number == 0: # '0' 정수
    print("'integer number'")
else: # '0' 이외
    if number % 1 == 0: # 정수
        if number < 0: # 음의 정수
            print("'Integer number'")
        else:
            print("'integer number'" ,end = " ")
            print("'natural number'" ,end = " ")
            if number % 2 == 0: # 짝수
                print("'even number'")
            else: # 홀수
                print("'odd number'")
            
    else: # 실수
        print("'float number'")
