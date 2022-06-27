#!/usr/bin/python

import sys

def calculator(nbr_1: int, nbr_2: int) -> None:
	print("Sum :" + str(nbr_1 + nbr_2))
	print("Difference : " + str(nbr_1 - nbr_2))
	print("Product : " + str(nbr_1 * nbr_2))
	print("Quotient : " + str(nbr_1 / nbr_2))
	print("Remainder : " + str(nbr_1 % nbr_2))

if len(sys.argv) != 3:
	print("Error")
	exit(-1)
if sys.argv[1].isdigit() == 0 or sys.argv[2].isdigit() == 0:
	print("Only numbers")
	exit(-1)
calculator(int(sys.argv[1]), int(sys.argv[2]))