#!/usr/bin/python

import sys

if len(sys.argv) != 2:
	print("error")
else:
	if sys.argv[1].isnumeric() == 0:
		print("error")
		exit
	num = int(sys.argv[1])
	if num == 0:
		print("Is zero")
	elif num % 2 == 0:
		print("Is even")
	else:
		print("Is odd")