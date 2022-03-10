import sys

args_len = len(sys.argv)


def upper_and_lower(st):
    for letter in st:
        if letter.islower():
            print(letter.upper(), end="")
        else:
            print(letter.lower(), end="")


concat = ' '

if args_len == 2:
    upper_and_lower(sys.argv[1])
else:
    concat.join(sys.argv[1:])
print(concat)
