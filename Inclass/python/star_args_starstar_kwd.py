import sys

def f(x,*args,file,**kwd):
	print(args)
	print(kwd)
	print(x)
	print(file)

# See below for difference bet'n arguments and keywords.
#    args     |       key words
f(4,5,6,"this",one="that",file=sys.stdout, sep=12)