# Sep.13 lec note 2021  Chuwei Chen


a = 6/4  # decimal division
b = 6//4  # integral division
c = 6 % 4  # Remainder
print(a, " ", b, ' ', c)

b = "that"
print(id(b))
print(hex(id(b)))


def b(x):
    print(x)


b("asdasd")


# Problem Starts Here
""" solve the quadratic equation

ax^2 + bx + c = 0

by asking the user for a,b,c

"""
"""
import math

a = int(input("please enter value for factor a: "))
b = int(input("please enter value for factor b: "))
c = int(input("please enter value for factor c: "))
#assert b**2-4*a*c>0, "invalid input"
if (b**2-4*a*c<0):
	print("invalid input")
else:
	x1 = (-b+math.sqrt(b**2 - 4*a*c))/(2*a)
	x2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)
	print("Your answer is follwing: x1 = ",x1,"x2 = ",x2)
"""
# Professor's code
names = ['a', 'b', 'c']
coefficient = []

for let in names:
    # in f-string, expressions are delimited by curly bracket {}
    a = input(f"Please enter {let}: ")
    coefficient.append(float(a))

a, b, c = coefficient
disc = b**2-4*a*c
if disc < 0:
    d1 = 1j*math.sqrt(abs(disc))
else:
    d1 = (b**2-4*a*c)**0.5

#d2 = math.sqrt(b**2 - 4*a*c)
root1 = (-b + d1) / (2 * a)
root2 = (-b - d1) / (2 * a)
print(f"The roots are {root1} and {root2}")
breakpoint()  # Debugger NOW, dir() to show commands
