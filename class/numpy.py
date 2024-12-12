import numpy as np
import matplotlib.pyplot as plt

arr = (1,2,3,4,5)
arrA = np.array([6,7,8,9,10])
arrB = np.array([[1,2],[3,4]])
arrC = np.array([[5,6],[7,8]])

print(sum(arr))
print(np.sum(arrA))
print(np.mean(arrA))

print(np.dot(arrB,arrC))

#============================================

x = np.linspace(-10,10,100)
y1 = x
y2 = x**2
y3 = np.sin(x)

plt.plot(x,y1,label='1')
plt.plot(x,y2,label='2')
plt.plot(x,y3,label='3')
plt.legend()
plt.show()