#!/usr/bin/env python
fill = 'q'
edge = '*'
W=2
T=2
H=5

full_edge = edge*W
top_box = ''
for lines in range(T):
	top_box += full_edge + "\n"

mid_box = " "
for lines in range(H-2*T):
	line = edge*T + fill(W-2*T) + edge*T
	mid_box += line+"\n"

the_box = top_box + mid_box + top_box
print(the_box)
	