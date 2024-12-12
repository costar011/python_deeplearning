# continue & break

absent = [2, 5] # 결석
no_book = [7] # 책을 안가져옴

for student in range(1, 11): # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    if student in absent:
        continue # 아래 코드를 실행하지 않고 다음 반복으로 넘어감
    
    elif student in no_book:
        print("오늘 수업 여기까지. {0}, 교무실로 따라와".format(student))
        break # 반복문을 탈출함 # continue와 break는 반복문에서만 사용 가능
    print("{0}, 책을 읽어봐".format(student))