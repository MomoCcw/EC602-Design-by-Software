class Toilet():
	def __init__(self):
		# pre-double-underscore means private in python
		# only accessible within the class
		self.__sex = "male"

	# Protected method
	def _Print(self):
		print(self.__sex)

wc = Toilet()
# print(wc.__sex)
wc._Print()





print(dir(wc))

shit = [1,2,5,3,2,324,234,23,3]
roundShit = ('asdfasdg',234,2348)

a, *_, b = shit

print(a,b)



a, *_ , c = roundShit

print(a,c)