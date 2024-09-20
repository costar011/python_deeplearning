# 표준입출력 

# import sys
# print("Python", "Java", file=sys.stdout)
# print("Python", "Java", file=sys.stderr)

# 시험 성적
scores = {"수학":0, "영어":50, "코딩":100}

# for subject, score in scores.items():
    # print(subject, score)
    # print(subject.ljust(8), str(score).rjust(4), sep=":") # ljust(8) : 8칸의 공간을 확보하고 왼쪽 정렬, rjust(4) : 4칸의 공간을 확보하고 오른쪽 정렬

# 은행 대기순번표
# 001, 002, 003, ...

# for num in range(1, 21):
    # print("대기번호 : " + str(num).zfill(3)) # zfill(3) : 3칸의 공간을 확보하고 빈 공간은 0으로 채움 # 001, 002, 003, ...

# answer = input("아무 값이나 입력하세요 : ") # input으로 입력받은 값은 항상 문자열로 저장됨
answer = 10
print(type(answer))
print("입력하신 값은 " + answer + "입니다.")