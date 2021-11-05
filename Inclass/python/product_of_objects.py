# 000
# 999
#
a=['one','two','three','four']

b=range(5)

c=(9,-1,2)

#one 0 9
#...
#four 4 2

S = [4,5,3]


def next_value(current, S):
    "[0,0,0] -> next one [1,0,0]"
    N = current[:]
    i = 0
    N[i] += 1
    while N[i]==S[i]:
        N[i] = 0
        i += 1
        if i==len(N):
            break
        N[i] += 1


    return N

c =[0,0,0]

for i in range(60):
    print(c)
    c = next_value(c,S)

def product(S):
    N = [0]*len(S)
    i = 0
    N[i] += 1
    while N[i]==S[i]:
        N[i] = 0
        i += 1
        if i==len(N):
            break
        N[i] += 1