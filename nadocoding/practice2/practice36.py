# 예외처리

# 어떤 에러가 발생했을 때 그에 대해서 처리를 해주는 것을 예외처리라고 한다.
# 예외처리를 사용하면 프로그램이 죽지 않고 계속 실행할 수 있다.

try:

print("나누기 전용 계산기입니다.")
num1 = int(input("첫 번째 숫자를 입력하세요: "))
num2 = int(input("두 번째 숫자를 입력하세요: "))

print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))

except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print("알 수 없는 에러가 발생하였습니다.")
    print(err)