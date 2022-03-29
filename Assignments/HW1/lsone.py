# Copyright 2021 Chuwei Chen chenchuw@bu.edu

import os

path = '..'

files = os.listdir(path)
sortedfiles = sorted(files)
for i in sortedfiles:
	print (i)

