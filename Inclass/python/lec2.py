#Sep.15 lec Chuwei Chen

#!/usr/bin/env python

def box(w,h,e,f):

	return "**"

default_edge = '#'

def main():
	"testcode"
	print (box(1,2,3,4))

if __name__ == '__main__':
	main()

# import sys
# a = input("what is a")

# try:
# 	result = float(a)
# except:
# 	print("this is not a number", file = sys.stderr)
# 	sys.exit(2)

import subprocess

T=subprocess.run(['ls'],stdout = subprocess.PIPE)
print(T)
print(T.stdout)

import sys

# to stdout
# print('hello')
# print('world',file=sys.stdout)
# sys.stdout.write("again\n")

# #from stdin
# a = input("what is it?")
# print("ok",a,2**16)
# for line in sys.stdin:
# 	print(line,"was typed")

# # to stderr
# print("this is an error", file=sys.stderr)
# sys.stderr.write("more problems\n")

import os 
print(os.listdir())

