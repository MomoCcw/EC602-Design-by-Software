import os
st=os.stat("/bin")
print (st)

g=st.st_mode

digits=[]
while g>0:
	digit =g % 8
	g = g//8
	digits.append(bin(digit))

print (digits)