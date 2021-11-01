# p(x) = 3x^5 + 1.2 x^2 +9
# Representing this information

class Polynomial:
	pass

s = "3x^5 + 1.2 x^2 + 9"
# option 1
# dictionary
# dictionary: key == power/exponent, value = coefficient
p = {5:3,2:1.2,0:9}

# option 2
# list with index meaning exponent
p = [3,0,0,1.2,0.9]
print(p)

# option 3
# paired table
coeff = [3,1.2,9]
power = [5,  2,0]

# option 4
# 2d array
poly = [[3, 1.2, 9], [5,  2, 0]]