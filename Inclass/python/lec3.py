#Sep.20th Chuwei Chen

'''
1. sort based on digits+letters only, ignoring symbols and capitalization
2. now sort on lower then upper.
3. symbols, then digits, then letters
4. Blank always come before (shorter comes before)
5. Column width: longest element +2
'''

#Sequences: List, tuple, str, range

l = list()
l = ['a',1,234]
t = tuple()
t = (1,2,3,9,"test")
s = str()
s = "abcdef"
r = range (10)
print(l,t,s,r)

# can you add to them: only lists
l.append('test')
print (l)
# str, tuple, range are immutable
s = s + "more"
print (s)

#iterate:
for item in l:
	print (item)
for item in r:
	print(item)
for i in t:
	print(i)
for i in s:
	print(i)

#typing
def print_this(x):
	print('printing',x)
	for item in x:
		print(item)

print_this(l)
print_this(r)

# print multiple lists
for seq in [l,r,s,t]:
	print_this(seq)

t = tuple(range(20))
print(t)

for i in range(20):
	print(t[i])

import string
letters=string.ascii_lowercase
print(repr(letters))
for i in range(26):
	print(i,letters[i])

#slicing

t = tuple(range(100))

first_ten = t[:10]
print(first_ten)

evens = t[::2]
print(evens)
odds = t[1::2]
print(odds)
print(t[4:9])

# t[:end]
# t[start:]
# t[start:end]
# t[start:end:step]
# t[::step]
# t[:end:step]
# t[start::]

# start default is 0
# step default is 1

ends_in_two = t[::10]
try: 
	print(t[2],t[3],t[4],t[100])
except:
	print('bad')

# slicing a sequence gives back the same kind of sequence
print(t[5:1000:5])
print(t[200:])

from os import listdir

files = listdir()
print(files[:5])

#magic negatives

print(t[-5:])
print(t[:-10])
print(t[-20:5:-1])
print(t[-5:-20:-2])