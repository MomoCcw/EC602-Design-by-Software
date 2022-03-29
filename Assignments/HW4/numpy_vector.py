import numpy as np

list1 = [5,6,9]
list2 = [1,2,3]
vector1 = np.array(list1)
vector2 = np.array(list2)
dot_product = vector1.dot(vector2)
scalar_mul = vector1 * 2
list3 = list1 + list2
print(vector1[0])
print(list3)
print(dot_product)
print(scalar_mul)
print(type(vector2),"  ",vector2[0])
print(np.linalg.norm(vector1))
print()

#input from tennisball
p = np.array([4.1,-4.1,4])
v = np.array([-1.2,5,1])

ans = v-2*(np.dot(v,p))/(np.dot(p,p))*p
print(ans)

ans = np.linalg.norm(np.array([-1.2,5,1]))
print(np.linalg.norm(np.array([-1.2,5,1])))
print(0.5*(ans**2)*3.1)
