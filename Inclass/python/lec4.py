#Sep.22th Chuwei Chen

s = 'this is a string with 912 spaces and numbers 123 sometimes sysbols #! also'
#remove all but letters

def remove_all(x,lose_these=None,keep_these=None):

	keepers = []
	for let in x:
		if let in keep_these:
			keepers.append(let)
	return "-".join(keepers)

def remove_all(x,lose_these=None,keep_these=None):
	"list comprehension"
	keepers = [let for let in x if let in keep_these]
	return "".join(keepers)

def remove_all(x,lose_these=None,keep_these=None):
	"I think this is too hard to read.!"
	return "".join([let for let in x if let in keep_these])

def remove_all(x,lose_these=None,keep_these=None):
	mylist = []
	ind = 0
	for i in range(len(x)):
		if x[i] in keep_these:
			mylist[ind] = x[i]
			ind += 1
	return mylist


def remove_all(x,lose_these=None,keep_these=None):
	"list comprehension"
	keepers = []

import string
theletters = string.ascii_lowercase

s=remove_all(s,keep_these=theletters)

print (s)

"""
Dictionary:

In [10]: history
d = dict()
hisotry
history
d['apple']=12
d['kiwi']=9
d[56]="value"
d
d['apple']=None
d
history

In [11]: d
Out[11]: {'apple': None, 'kiwi': 9, 56: 'value'}
"""
