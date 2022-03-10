######################################################################
################## Exercise 04 - operations.py #######################

import sys

def add(n1, n2):
    return n1 + n2

def diff(n1, n2):
    return n1 - n2

def product(n1, n2):
    return n1 * n2

def div(n1, n2):
	return n1 / n2

def mod(n1, n2):
    return n1 % n2


def ops(arg1, arg2):
	Sum = add(int(arg1),int(arg2))
	Diff = diff(int(arg1),int(arg2))
	Product = product(int(arg1),int(arg2))
	Div = div(int(arg1),int(arg2))
	Mod = mod(int(arg1),int(arg2))

	print("Sum: {0}\nDifference: {1}\nProduct: {2}\nQuotient: {3}\nRemainder: {4}".format(Sum, Diff, Product, Div, Mod))

if len(sys.argv) == 3:
    ops(sys.argv[1], sys.argv[2])
elif len(sys.argv) < 3:
	print("NOT ENOUGH ARGUMENTS !")
else:
	print("ENTER ONLY 2 ARGUMENTS !")