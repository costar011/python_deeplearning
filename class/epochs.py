import numpy as np
import matplotlib.pyplot as plt

X = np.array([0.0, 1.0, 2.0])
y = np.array([3.0, 3.5, 5.5])

W = 0 #기울기
b = 0 #절편

lrate = 0.01 # 학습률
epochs = 1000 # 반복 횟수

n = float(len(X)) #입력 데이터의 개수

# 경사 하강법
for i in range(epochs):
    y_pred = W * X + b # 예측 값
    dW = (2/n) * sum(X * (y_pred-y))
    db = (2/n) * sum(y_pred-y)
    W = W - lrate * dW # 기울기 수정
    b = b - lrate * db # 절편 수정

    
print(W,b) # 기울기, 절편 출력

y_pred = W * X + b # 예측 값

plt.scatter(X, y) # 입력데이터를 그래프 상에 찍는다
plt.plot([min(X), max(X)], [min(y_pred), max(y_pred)], color='red')
plt.show()