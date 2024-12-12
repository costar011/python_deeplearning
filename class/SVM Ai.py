import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore',category=UserWarning)
import cvxpy as cvx

'''
x1, x2: 두 개의 특징을 가진 데이터 포인트를 나타내는 NumPy 배열
xp, ypt: 실제 분류 경계선을 나타내는 선형 방정식
g, g1, g0: 데이터 포인트를 두 클래스로 분류하기 위한 임계값을 정의하는 함
'''
x1= np.array([[1], [7.8], [5.2],[7.3],[0.5],[2.6],[4.7],[4.6],[1.5], [4.1]])
x2= np.array([[0.5],[-4.5],[3.3],[0.2], [4],[-3], [-2], [0.5],[ 3.8], [2]])
xp = np.linspace(-1,9,100).reshape(-1,1)
ypt = -0.8*xp + 3
plt.plot(x1, x2, 'ro', alpha = 0.4)
plt.plot(xp, ypt, label = 'True')
plt.xlim([0, 10])
plt.ylim([-5, 5])
g = 0.8*x1 + x2 - 3
g1 = g - 1
g0 = g + 1
C1 = np.where(g1 >= 0)[0]
C0 = np.where(g0 < 0)[0]
plt.plot(x1[C1], x2[C1], 'ro', alpha = 0.4, label = 'C1')
plt.plot(x1[C0], x2[C0], 'bo', alpha = 0.4, label = 'C0')
xp = np.linspace(-1,9,100).reshape(-1,1)
ypt = -0.8*xp + 3
plt.plot(xp, ypt, 'k', linewidth = 3, label = 'True')
plt.plot(xp, ypt-1, '--k')
plt.plot(xp, ypt+1, '--k')

'''
w0, w: 선형 분류기의 가중치를 나타내는 CVXPY 변수
obj: 목적 함수 (최대화 문제이지만, 실제로는 제약 조건만 만족하는 해를 찾는 문제)
const: 제약 조건
'''
X1 = np.hstack([x1[C1], x2[C1]]) # 새로운 배열 생성, 배열들을 수평으로 연결(np.hstack)
X0 = np.hstack([x1[C0], x2[C0]])
w0 = cvx.Variable([1,1])
w = cvx.Variable([2,1])
obj = cvx.Maximize(1)
const = [w0 + X1*w >= 1, w0 + X0*w <= -1]
'''
w0 + X1*w >= 1: 클래스 C1의 데이터 포인트는 분류 경계선으로부터 1 이상 떨어져 있어야 함
w0 + X0*w <= -1: 클래스 C0의 데이터 포인트는 분류 경계선으로부터 -1 이하로 떨어져 있어야 함
'''

prob = cvx.Problem(obj, const).solve() # CVXPY 문제를 풀어 최적의 w0와 w를 구함

w0 = w0.value # 최종 w0 값
w = w.value # 최종 w 값
xp = np.linspace(-1,9,100).reshape(-1,1)
yp = - w[0,0]/w[1,0]*xp - w0/w[1,0]

# 구해진 w0와 w를 이용하여 예측된 분류 경계선을 계산하고 시각화
for i in range(len(x1)): # 배열 크기만큼 반복
    plt.text(x1[i], x2[i], f"({x1[i][0]:.1f}, {x2[i][0]:.1f})", fontsize=8) 

plt.plot(x1[C1], x2[C1], 'ro', alpha = 0.4, label = 'C1') 
plt.plot(x1[C0], x2[C0], 'bo', alpha = 0.4, label = 'C0')
# 클래스에 속하는 데이터 포인트 x,y 좌표

plt.plot(xp, ypt, 'k', alpha = 0.3, label = 'True')
plt.plot(xp, ypt-1, '--k', alpha = 0.3)
plt.plot(xp, ypt+1, '--k', alpha = 0.3)
plt.plot(xp, yp, 'b', linewidth = 3)
plt.plot(xp, yp-1, 'b', linewidth = 1)
plt.plot(xp, yp+1, 'b', linewidth = 1)
plt.xlabel(r'$x_1$', fontsize = 15)
plt.ylabel(r'$x_2$', fontsize = 15)
plt.legend(loc = 1)
plt.axis('equal')
plt.xlim([0, 8])
plt.ylim([-5, 5])
plt.show()