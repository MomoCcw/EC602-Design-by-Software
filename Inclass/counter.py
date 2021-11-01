c = [3,5,4]

def countem(c):
    a=[0]* len(c)
    while True:
        yield a
        j=0
        a[j] += 1
        while a[j]==c[j]:
            a[j]=0
            j += 1
            if j == len(c):
              return
            a[j]+=1


for x in countem(c):
    print(x)
