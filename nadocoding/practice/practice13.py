# 세트 (set) 집합
# 중복이 허용되지 않는다. 순서가 없다.

my_set = {1, 2, 3, 3, 3}
print(my_set) # {1, 2, 3}

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"]) # 리스트로 선언해서 set으로 변환

# 교집합 (java와 python을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python)) # 둘 다 가능한 개발자

# 합집합 (java 할 수 있거나 python 할 수 있는 개발자)
print(java | python)
print(java.union(python)) # union 합집합 

# 차집합 (java 할 수 있지만 python은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python)) # 차집합

# python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

# java를 잊었어요
java.remove("김태호")
print(java)