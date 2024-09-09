# while

customer = "토르"
index = 5

# while 조건문 : 어떤 조건이 만족할 때까지 반복하는 것

while index >= 1: # index가 1 이상일 때까지 반복
    print("{0}, 커피가 준비되었습니다. {1}번 남았어요.".format(customer, index))
    index -= 1 # index를 1씩 감소시킴
    if index == 0: # index가 0이 되면
        print("커피는 폐기처분되었습니다.") # 커피는 폐기처분되었습니다. 