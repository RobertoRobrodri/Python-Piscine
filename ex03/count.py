#!/usr/bin/python

import sys

def text_analyzer(string: str) -> None:
	n_up = n_low = n_spc = 0
	for x in string:
		if x.isupper():
			n_up += 1
		elif x.islower():
			n_low += 1
		elif x.isspace():
			n_spc += 1
	print("Uppercase = " + str(n_up))
	print("Lowercase = " + str(n_low))
	print("Spaces = " + str(n_spc))

n_args = len(sys.argv)
if n_args < 2:
	text = input("Type something: ")
elif n_args > 2:
	print("Error")
	exit()
else:
	text = sys.argv[1]
text_analyzer(text)