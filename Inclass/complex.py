# Complex Numbers:
# Complex is a new type of object

#Simplest possible new type
# class Complex():
	
# 	pass # for a new function block, put pass in it 
# 		 #if not yet knowing what to put in it
class Complex():
	"this is a new type"
	def __init__(self,x,y):
		print("in init")
		self.x=x
		self.y=y
		pass

	def f(self):
		print('f',self)
		print(self.x,self.y)

print('making c')
c = Complex(3,4)
print('making b')
b = Complex(6,7)
print(b,c)

b.real = 12
b.imag = 24
print(b.real + b.imag)

c = complex(3,4)
print(c)


c = Complex(6,7)
Complex.__init__(c,0,0)
print(c,c.x,c.y)