# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램 작성
# 예) http://naver.com

# 규칙1) http:// 부분은 제외
#   > naver.com

# 규칙2) 처음 만나는 점(.) 이후 부분은 제외
#   > naver

# 규칙3) 남은 글자 중 처음 세자리(nav) + 글자 개수(5) + 글자 내 'e' 개수(1) + "!"(!)로 구성
#   > 생성된 비밀번호 : nav51!

url = "http://naver.com"

my_str = url.replace("http://", "")  # 규칙1
# print(my_str)  # naver.com

my_str = my_str[:my_str.index(".")]  # 규칙2
# my_str[:my_str.index(".")] -> my_str 문자열에서 처음부터 '.'이 나오기 전까지 문자열을 반환
print(my_str)  # naver

password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0} 의 비밀번호는 {1} 입니다.".format(url, password)) 
# http://naver.com 의 비밀번호는 nav51! 입니다.