# 지역변수와 전역변수

# 지역변수: 함수 내에서만 사용하는 변수
# 전역변수: 프로그램 전체에서 사용하는 변수

gun = 10

def checkpoint(soldiers): # 경계근무
    global gun # 전역 공간에 있는 gun 사용 # 전역변수
    gun = gun - soldiers # 총에서 군인 수만큼 빼기 # 지역변수
    print("[함수 내] 남은 총: {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총: {0}".format(gun))
    return gun

print("전체 총: {0}".format(gun))
# checkpoint(2) # 2명이 경계근무 나감
gun = checkpoint_ret(gun, 2) # 2명이 경계근무 나감
print("남은 총: {0}".format(gun)) # 전체 총 출력