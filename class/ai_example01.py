import matplotlib.pyplot as plt
import numpy as np
data = np.array([[2,2],
                 [7,7],
                 [14,3],
                 [8,9],
                 [15,5],
                 [3,2]])

center = np.array([data[0], data[2], data[4]])

plt.scatter(data[:,0], data[:,1]) # 동그라미
plt.text(2.3,2.5,'1:(2,2) center')
plt.text(7.3,7,'2:(7,7)')
plt.text(14.3,3,'3:(14,3) center')
plt.text(8.3,9,'4:(8,9)')
plt.text(15.3,5,'5:(15,5) center')
plt.text(3.3,2,'6:(3,2)')

plt.scatter([2,14,15],[2,3,5], marker="*", s=200) # 별
plt.axis([0,20,0,12])
plt.show()

# 거리계산
print("==== 거리 계산 ====")
print("data[1]\t\t\t\t\t\t: ",data[1])
print("center[0]\t\t\t\t\t: ",center[0])
print("center[0] - data[1]\t\t\t\t: ",center[0] - data[1])
print("(center[0] - data[1])^2\t\t\t\t: ",(center[0] - data[1])**2)
print("((center[0] - data[1])^2).sum()\t\t\t: ",((center[0] - data[1])**2).sum())
print("np.sqrt(((center[0] - data[1])^2).sum())\t: ",np.sqrt(((center[0] - data[1])**2).sum()))
print("==== 거리 계산 끝 ====")

dis = np.zeros((6,3))

for i in range(6):
    for j in range(3):
        dis[i][j] = np.sqrt(((center[j] - data[i])**2).sum())
        
# MIN INDEX
minIdx = np.zeros(6)
tmp = 0
for i in range(6):
    tmp = dis[i][0]
    idx = 0
    for j in range(3):
        if tmp > dis[i][j]:
            tmp = dis[i][j]
            idx = j
        minIdx[i] = idx
        
# minIdx별 센터 구하기
tmpCen0 = []
tmpCen1 = []
tmpCen2 = []

for i in range(6):
    if minIdx[i] == 0:
        tmpCen0.append(data[i])
    if minIdx[i] == 1:
        tmpCen1.append(data[i])
    if minIdx[i] == 2:
        tmpCen2.append(data[i])
        #=====================================================
        
        
# center 좌표 구하기
tmpCen0 = np.array(tmpCen0)
tmpCen0 = tmpCen0.mean(axis=0)

tmpCen1 = np.array(tmpCen1)
tmpCen1 = tmpCen1.mean(axis=0)

tmpCen2 = np.array(tmpCen2)
tmpCen2 = tmpCen2.mean(axis=0)

center = [tmpCen0, tmpCen1, tmpCen2]
center = np.array(center)

# 1단계 그림
plt.scatter(data[:,0], data[:,1])
plt.text(2.3,2.5,'1:(2,2)')
plt.text(7.3,7,'2:(7,7)')
plt.text(14.3,3,'3:(14,3)')
plt.text(8.3,9,'4:(8,9)')
plt.text(15.3,5,'5:(15,5)')
plt.text(3.3,2,'6:(3,2)')

for i in range(3):
    plt.scatter(center[i][0],center[i][1],marker="*",s=200)
plt.axis([0,20,0,12])
plt.show()

# 2단계 거리 구하기
dis = np.zeros((6,3))

for i in range(6):
    for j in range(3):
        dis[i][j] = np.sqrt(((center[j] - data[i])**2).sum()) # 루트안에 센터 - 데이터 값을 뺀후 제곱을 해주고 소수점으로 나타낸다.

# 2단계 min idx 구하기
minIdx = np.zeros(6)
tmp = 0
for i in range(6):
    tmp = dis[i][0]
    idx = 0
    for j in range(3):
        if tmp > dis[i][j]:
            tmp = dis[i][j]
            idx = j
    minIdx[i] = idx
    
# 2단계 센터 구하기
# minIdx 별 센터 구하기
tmpCen0 = []
tmpCen1 = []
tmpCen2 = []

for i in range(6):
    if minIdx[i] == 0:
        tmpCen0.append(data[i])
    if minIdx[i] == 1:
        tmpCen1.append(data[i])
    if minIdx[i] == 2:
        tmpCen2.append(data[i])