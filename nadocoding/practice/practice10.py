# 리스트 []
# 순서가 있는 수정 가능한 객체의 집합

# 지하철 칸별로 10명, 20명, 30명
# subway1 = 10
# subway2 = 20
# subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"] # [0 , 1, 2]
print(subway)

# 조세호씨가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))  # 1번째 위치

# 하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하") # append -> 뒤에 더하다는 의미 
print(subway)

# 정형돈씨를 유재석 / 조세호 사이에 태워봄
subway.insert(1, "정형돈") # insert -> 원하는 위치에 추가
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop()) # pop -> 뒤에서 꺼내기
print(subway)

# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석")) # count -> 몇 개 있는지 확인

# 정렬도 가능
num_list = [5, 2, 4, 3, 1]
num_list.sort() # sort -> 정렬
print(num_list)

# 순서 뒤집기 가능
num_list.reverse() # reverse -> 뒤집기
print(num_list)

# 모두 지우기
num_list.clear() # clear -> 모두 지우기
print(num_list)

# 다양한 자료형 함께 사용
num_list = [5, 2, 4, 3, 1]
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장
num_list.extend(mix_list) # extend -> 확장
print(num_list)