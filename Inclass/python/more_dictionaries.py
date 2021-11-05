# 

D = {4:5, "apple":6, (4,3):"test"}
print(D)
print('\n')
for key in D:
    print(key,D[key])
print('\n')


for item in D.items():
    print(item)
print('\n')

for key,value in D.items():
    print(key,value)
print('\n')


for value in D.values():
    print(value)
print('\n')

L = [4 , 5, 7]

for ind,item in enumerate(L):
    print(ind,item)
print('\n')

for i in range(len(L)):
    print(i,L[i])
print('\n')

for i in range(5):
    print(i,D.get(i,"None"))
print('\n')
