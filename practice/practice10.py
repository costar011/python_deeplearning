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