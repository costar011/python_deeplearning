x1a, x2a = map(float, input("X1, X2 입력 >> ").split())
x1b, x2b = map(float, input("X1, X2 입력 >> ").split())

dist = ((x1a - x1b) ** 2 + (x2a - x2b) ** 2) ** 0.5
strDist = "{0:0.2f}".format(dist)
print("두 점의 거리 >> ", strDist)