# define a class that 
# is like a list but does not
# allow for the addition of 0
#
class NoZeroList(list):
    def append(self,newitem):
        print(f'adding {newitem}')
        super().append(newitem)
    pass

g=NoZeroList()
g.append("1")
g.append(4)
print(g)
g.append(0)