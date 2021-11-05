#Sep 29th Chuwei Chen

import os
s1 = os.stat('HW1')
s2 = os.lstat('HW1')

s3 = os.stat('sort_order_testing')
s4 = os.lstat('sort_order_testing')
print(s1,s2,s3,s4)

for fcn in [os.stat,os.lstat]:
    for fname in 'HW1','sort_order_testing':
        print(fcn,fname)
        res = fcn(fname)
        print(res)
        print(res.st_blocks)
        print()

# Simplest possible new type
class Complex():
	"this is a new type"
	def __init__(self,x,y):
		print("in init (creating new object)")
		self.x=x
		self.y=y

	def add(self,other):
		return Complex(self.x+other.x,self.y+other.y)
			# / in the end means arguments MUST BE POSITIONAL
	def __add__(self,value,/):
		"try to handle ints with explicit test"
		if isinstance(value,int) or isinstance(value,float):
			other = Complex(value,0)
			return self+other
		return Complex(self.x+value.x,self.y+value.y)

	def __add__(self,value,/):
		if hasattr(value,"y") and hasattr(value,"x"):
			return Complex(self.x+value.x,self.y+value.y)
		else:
			return Complex(self.x+value, self.y)

	# def __radd__(self,value,/):
	# 	print("reverse adding",self,value)
	# 	if hasattr(value,"y") and hasattr(value,"x"):
	# 		return Complex(self.x+value.x,self.y+value.y)
	# 	else:
	# 		return Complex(self.x+value, self.y)

	__radd__ = __add__

	# Callable.
	def __call__(self):
		print("asd")

# function for adding complex numbers
def add(y: Complex, z: Complex) -> Complex:
	real = y.x+z.x 
	imag = y.y+z.y
	return Complex(real,imag)

def print_complex(c):
	print(f"({c.x} + j{c.y})")

# Operations, printing

a = Complex(4,5)
b = Complex(8,1.5)
c = add(a,b)
print_complex(c)
d = a.add(b)
# 0. single letter names only ok when used in examples
# 1. looks like append
# 2. is 'a' modified? not clear
# 3. looks asymmetrical
# 4. not math
print_complex(d)

w = a+b 
print_complex(w)

z = a + 1.0
print_complex(z)

c = Complex("this","that")
d = Complex("one","two")

e = c+d
print_complex(e)

w = 1.0 + a
print_complex(w)

w()