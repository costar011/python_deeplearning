import copy
# [ 함수 ] #

# 중심점 출력
def printMidPoints(midPoints):
    print()
    for i in range(len(midPoints)):
        print("c{0}\t{1}\t{2}".format(i+1, midPoints[i][0], midPoints[i][1]))

# 거리표 출력
def printDistances(distances):
    print()
    ## 표 제목 출력
    print("", end="\t")
    for i in range(len(distances[0])):
        print(i+1, end="\t")
    print()

    ## 거리 데이터 출력
    for i in range(len(distances)):
        listTemp = list(map(str, distances[i]))
        print("c{0}\t".format(i+1), end="") # c1 ~ cn 출력
        print("\t".join(listTemp)) # 거리 데이터 출력

# 거리표 계산
def computeDistances(data, midPoints):
    distances = []
    distTemp = []
    for k in midPoints:
        for i in range(len(data)):
            dist = ((k[0] - data[i][0]) ** 2 + (k[1] - data[i][1]) ** 2) ** 0.5
            dist = float("{0:0.2f}".format(dist))
            distTemp.append(dist)
        distances.append(distTemp)
        distTemp = []
    printDistances(distances) # 거리표 출력
    return distances

# 거리표 기준으로 그룹 결정
def getGroups(distances, groupCount):
    groups = [
        []
        for _ in range(groupCount)
    ]
    for i in range(len(distances[0])):
        minIdx = 0
        for j in range(1, len(distances)):
            if distances[j][i] < distances[minIdx][i]:
                minIdx = j
        groups[minIdx].append(i)

    # 결정된 그룹 출력
    print()
    for i in range(len(groups)):
        listTemp = copy.deepcopy(groups[i])
        for j in range(len(listTemp)):
            listTemp[j] += 1
        listTemp = list(map(str, listTemp))
        print("c{0} =".format(i+1), "{", ", ".join(listTemp), "}")
        
    return groups

# 그룹을 기준으로 중심점 계산
def getMidPoints(data, groups):
    midPoints = []
    for k in groups:
        sumX = 0
        sumY = 0
        for l in k:
            sumX += data[l][0]
            sumY += data[l][1]
        midX = float("{0:0.1f}".format(sumX / len(k)))
        midY = float("{0:0.1f}".format(sumY / len(k)))
        midPoints.append([midX, midY])
    printMidPoints(midPoints) # 중심점 출력
    return midPoints

# 두 배열이 같은지 비교
def isArrayEqual(array1, array2):
    try:
        for i in range(len(array1)):
            for j in range(len(array1[i])):
                if array1[i][j] != array2[i][j]:
                    return False
        return True
    except:
        return False

# [ 코드 ] #

# 데이터 입력
data = []
while True:
    try:
        x1, x2 = map(float, input("X1, X2 >> ").split())
        data.append([x1, x2])
    except:
        break

# 분류 그룹 수 입력
while True:
    groupCount = int(input("분류 할 그룹 수 >> "))
    if groupCount > 0 and groupCount <= len(data):
        break
    print("분류 그룹 수가 올바르지 않습니다!")

# 최초 중심점 선택
midPoints = []
midPointsIdx = []
for i in range(groupCount):
    midPoints.append(data[i])
    midPointsIdx.append(i)
printMidPoints(midPoints) # 중심점 출력

# 그룹화 계산
groups = []
while True:
    distances = computeDistances(data, midPoints) # 거리표 계산
    newGroups = getGroups(distances, groupCount) # 거리표 기준으로 그룹 결정
    # 이전 그룹과 비교
    if isArrayEqual(newGroups, groups): # 같다면
        print("\n프로그램 종료")
        break
    # 같지 않다면
    groups = newGroups
    midPoints = getMidPoints(data, groups) # 중심점 계산