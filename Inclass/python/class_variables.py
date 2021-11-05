class Animal:
    _i = 0
    def __init__(self,name):
        self.name = name
        Animal._i += 1


    def count(self):
        "return the number of created animals"
        return Animal._i

    def __str__(self):
        return self.name

class Cat(Animal):
    pass

a = Animal("Ant")
print(f"{a.count()=}" )

c = Cat("Murphy")
print(f"{c._i=}")
print(f"{c.count()=}" )

c._i = 10
print(f"{c._i=}")
print(f"{c.count()=}" )
print(id(c._i),id(Animal._i),id(a._i))

print(a,c)