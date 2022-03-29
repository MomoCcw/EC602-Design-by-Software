# inheritance

class Animal():
    def __init__(self,name=""):
        print('animal init')
        self.name = name
    def __str__(self):
        return self.name

class Cat(Animal):
    def __init__(self,color="",name=""):
        print('cat init')
        self.color = color
        self.name = name

m = Cat("orange","Murphy")
print(m)