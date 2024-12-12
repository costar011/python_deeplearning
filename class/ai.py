# K-Mean 프로그램
# https://velog.io/@hyeongjun/%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D-%EC%82%AC%EC%9D%B4%ED%82%B7%EB%9F%B0sklearn-%EA%B8%B0%EC%B4%88
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs # type: ignore

# 예제 데이터 생성
X, y = make_blobs(n_samples=300, centers=4, random_state=42)

# KMeans 모델 생성
kmeans = KMeans(n_clusters=4, random_state=42)

# 모델 학습
kmeans.fit(X)

# 클러스터 레이블
labels = kmeans.labels_

# 클러스터 중심
centers = kmeans.cluster_centers_

# 결과 시각화
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', marker='o', edgecolor='k', s=50)
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.75, marker='X')  # 중심점 표시
plt.title('K-means Clustering')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()

#=========================================

# 데이터 입력
data = input("데이터를 입력하세요 (쉼표로 구분된 숫자): ")
data = np.array([float(i) for i in data.split(',')]).reshape(-1, 2)

# 클러스터 수 지정
n_clusters = int(input("클러스터 수를 입력하세요: "))

# KMeans 모델 생성 및 학습
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
kmeans.fit(data)

# 클러스터 레이블 및 중심
labels = kmeans.labels_
centers = kmeans.cluster_centers_

# 결과 시각화
plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis', marker='o', edgecolor='k', s=50)
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.75, marker='X')  # 중심점 표시
plt.title('K-means Clustering')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()