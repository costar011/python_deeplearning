import numpy as np

# 경사 하강법 구현 코드

import matplotlib.pyplot as plt

# 입력 데이터
X = np.array([0.0, 1.0, 2.0])  # 독립 변수
y = np.array([3.0, 3.5, 5.5])  # 종속 변수

# 초기화
W = 0  # 기울기
b = 0  # 절편

lrate = 0.01  # 학습률
epochs = 1000  # 반복 횟수

n = float(len(X))  # 입력 데이터의 개수

# 경사 하강법
for i in range(epochs):
    y_pred = W * X + b  # 예측 값
    dW = (2/n) * sum(X * (y_pred - y))  # 기울기의 변화량
    db = (2/n) * sum(y_pred - y)  # 절편의 변화량
    W = W - lrate * dW  # 기울기 수정
    b = b - lrate * db  # 절편 수정

# 기울기와 절편 출력
print(W, b)

# 예측 값을 만든다
y_pred = W * X + b

# 입력 데이터를 그래프 상에 찍음
plt.scatter(X, y)

# 예측 값은 그래프로 그림
plt.plot([min(X), max(X)], [min(y_pred), max(y_pred)], color='red')

plt.show()