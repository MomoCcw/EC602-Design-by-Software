# Chained less than

a = 5 < 12 < 10
print(a)
print()
class Thing():
    def __init__(self,n):
        self.name = n
    def __lt__(self,other):
        print('in lt',self.name,other.name)
        return len(self.name) < len(other.name)

a = Thing("one")
b = Thing('four')
c = Thing("three")

print(a < b < c)