# some numpy
import numpy as np

v1 = np.array([4,-1,2])
v2 = np.array([1,-2,5])

print(np.dot(v1,v2))

print(v1 @ v2)

A = np.array([[1,3,4],[5,6,1],[3,1,2]])
b = np.array([9,8,7])

x= np.linalg.solve(A,b)
print(x)
print(A @ x)