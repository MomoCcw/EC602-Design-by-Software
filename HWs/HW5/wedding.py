# Copyright 2021 Chuwei Chen chenchuw@bu.edu
# Copyright 2021 Zhaozhong Qi zqi5@bu.edu

class Wedding: 
	arrangements = []
    def __init__(self):
    	self.names = []
    	self.max_size = 0
    def shuffle(self, guests):
    	"return all possible arrangements of the guests specified as a list of strings"
    	max_size = len(guests)
    	for i in guests:
    		self.names.append(i)

    def barriers(self, guests, bars):
    	pass	






def  show_result(v, partial=False):
	v.sort()
	print("",len(v),"\n".join(v),sep="\n")

if __name__ == '__main__':
	standard = Wedding()
	res = standard.shuffle("abc")
	res = ["abc"]
	show_result(res)
