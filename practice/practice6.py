# 슬라이싱
jumin = "030522-4567890"

print("성별 : " + jumin[7]) # 성별 출력 / 7번째 자리의 문자 출력
print("연 : " + jumin[0:2]) # 연도 출력 / 0번째부터 2번째 직전까지의 문자 출력
print("월 : " + jumin[2:4]) # 월 출력 / 2번째부터 4번째 직전까지의 문자 출력
print("일 : " + jumin[4:6]) # 일 출력 / 4번째부터 6번째 직전까지의 문자 출력

print("생년월일 : " + jumin[:6]) # 생년월일 출력 / 처음부터 6번째 직전까지의 문자 출력
print("뒤 7자리 : " + jumin[7:]) # 뒤 7자리 출력 / 7번째부터 끝까지의 문자 출력
print("뒤 7자리 (뒤에부터) : " + jumin[-7:]) # 맨 뒤에서부터 끝까지 / 맨 뒷자리는 -1부터 시작