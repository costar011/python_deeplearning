# for (반복문)

# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")

# for waiting_no in [0, 1, 2, 3, 4]: # 리스트 형태로 대기번호 출력
   # print("대기번호 : {0}".format(waiting_no))

# for waiting_no in range(5): # 0, 1, 2, 3, 4
    # range 함수 사용 -> 0부터 5미만까지
   # print("대기번호 : {0}".format(waiting_no))

# randrange 함수 사용
for waiting_no in range(1, 6): # 1, 2, 3, 4, 5 / 1부터 6미만까지
    print("대기번호 : {0}".format(waiting_no))

starbucks = ["아이언맨", "토르", "그루트"]

for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer)) # 리스트에 있는 값들을 출력