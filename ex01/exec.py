#!/usr/bin/python

import sys

x = 1
while x < len(sys.argv):
	print(sys.argv[x][::-1].swapcase())
	x+=1