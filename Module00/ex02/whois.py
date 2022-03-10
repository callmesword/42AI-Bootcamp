################################################################
################## Exercise 02 - whois.py ######################


import sys

if len(sys.argv) > 1:
    n = int(sys.argv[1])
    if n % 2 == 0 and n != 0:
        print("I'm Even.")
    elif n == 0:
        print("I'm Zero")
    else:
        print("I'm Odd.")
