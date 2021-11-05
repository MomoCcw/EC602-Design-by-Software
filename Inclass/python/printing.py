class Complex():
    "printing focus"

    def __str__(self):
        return f"({self.x} +j + {self.y})"
    def __repr__(self):
        return "repr"
        return f"Complex({self.x},{self.y})"

def f(x):
    pass
c = Complex()
c.x, c.y = 5.6, 1.1

print(c)

d = Complex()
d.x,d.y = 1,-2
s = str(d)
print(f'{s=}')

c = 3-4j
print(c,f)

def this():
    pass

mywords = [5,"5",1.2,"1.2",'this','that',this,d]
print(mywords)
for word in mywords:
    print(word)
