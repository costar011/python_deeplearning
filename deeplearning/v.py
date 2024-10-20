import numpy as np
import cvxpy as cvx

f = np.array([[3], [3/2]])
lb = np.array([[-1],[0]])
ub = np.array([[2],[3]])

x = cvx.Variable((2,1))
'''
컨벡스 최적화 툴박스에서 2x1 크기의 변수 벡터 생성
Variable = 최적화 문제에서 값을 찾아야 할 변수 의미
    > x 라는 이름의 2차원 열 벡터를 하나 생성 후 이 벡터의 각 요소는 최적화 문제엣 찾아야 할 변수로 지정
'''

obj  = cvx.Maximize(f.T@x) # f와 x의 내적을 최대화하는 것은 벡터 f 방향으로 x를 최대한 멀리 이동
'''
Maximize = 목적 함수를 최대화
(f.T@x)
f.T = 벡터 f의 전치(tanspose)를 의미, 행벡터 f를 열벡터로 변환
@ = 행령의 곱셉 연산자
x = 최적화 문제에서 찾을려는 변수 벡터
    > 벡터 f, 벡터 x의 내적을 의미하고 나온 값은 스칼라 값이다. (f,x의 내적을 최대한 크게 만들 수 있는 x를 찾으라고 명령)
'''

const = [lb <= x,x<= ub] # lb와 ub는 x의 가능한 값의 범위를 제한합니다. 즉, x는 lb와 ub로 정의된 직사각형 영역 안

prob = cvx.Problem(obj,const)
'''
최적화 문제 생성
obj > 목적 함수 (최소화, 최대화)
const > 제약 조건 (변수가 만족해야 하는 조건)
    > 목적함수를 최소화(최대화)하고, const라는 제약 조건을 만족하는 최적화 문제를 생성 후 prob 변수에 저장
'''
result = prob.solve()
print(x.value)
print(result)