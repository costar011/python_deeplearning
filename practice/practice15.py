# if

weather = input("오늘 날씨는 어때요? ") # input() 함수는 사용자로부터 입력을 받는 함수
if weather == "비" or weather == "눈": # or는 둘 중 하나만 만족해도 true
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어요")



temp = int(input("기온은 어때요? ")) # input() 함수는 사용자로부터 입력을 받는 함수 / int() 함수는 문자열을 숫자로 변환하는 함수
if 30 <= temp:
    print("너무 더워요. 나가지 마세요")
elif 10 <= temp and temp < 30: # and는 둘 다 만족해야 true
    print("괜찮은 날씨에요")
elif 0 <= temp < 10:
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지 마세요")