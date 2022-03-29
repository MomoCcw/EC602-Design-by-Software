# slicing

from os import listdir
t = tuple(range(100))


first_ten = t[:10]
print(first_ten)

evens = t[::2]
print(evens)

odds = t[1::2]
print(odds)
# t[:end]
# t[start:]
# t[start:end]   start up to end - 1   end - start is number of values.
# t[start:end:step]
# t[:end:step]
# t[::step]
# t[start::]

print(t[4:9])

# start default is 0
# step default is 1


# All the numbers that end in 3
ends_in_two = t[::10]

# indexing past the end is a run time error.

try:
    print(t[2], t[3], t[4], t[100])
except:
    print('bad')

# slicing a sequence gives back the same kind of sequence
print(t[5:1000:5])

print(t[200:])


files = listdir()
print(files[:5])

# magic negatives

print(t[-5:])
print(t[:-10])
print(t[5:20:-1])
print(t[-20:-5:-1])
print(t[-5:-20:-2])
