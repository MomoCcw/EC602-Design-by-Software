#
#
# p(x) = 3x^5  + 1.2 x^2 + 9
#
#
#
# Representing this information.
#
# 3    5
# 1.2  2
# 9    0

s = "3x^5  + 1.2 x^2 + 9"

# Options


# option 1
# dictionary: key==power/exponent, value = coefficient

p = {5:3, 2:1.2, 0:9}

# option 2
# list with index meaning exponent
p = [3,0,0,1.2,0,9]
print(p)


# option 3
# paired table
coeff = [3, 1.2, 9]
power = [5,   2, 0]

# option 4
# 2d array
poly =[ [3, 1.2, 9], [5,   2, 0] ]






class Polynomial:
    pass

p = Polynomial()
print(p)