import sys
import string

lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase
puncs = string.punctuation


def text_analyzer(arg):
    analysis = {"lower": 0, "upper": 0, "punc": 0, "spaces": 0}
    # if len(sys.argv) < 2:
    #     promt = input("NO ARGUMENTS ! ENTER A TEXT: ")
    if len(sys.argv) == 2:
        for letter in arg:
            if letter == ' ':
                analysis['spaces'] += 1
            for lower in lower_case:
                if letter == lower:
                    analysis['lower'] += 1
            for upper in upper_case:
                if letter == upper:
                    analysis['upper'] += 1
            for punc in puncs:
                if letter == punc:
                    analysis['punc'] += 1
    display_result(analysis)
    return analysis


def display_result(result):
    chars_len = len(sys.argv[1])
    upper_chars = result['upper']
    lower_chars = result['lower']
    puncs = result['punc']
    spaces = result['spaces']
    print("The text contains {0} character(s):\n- {1} upper letter(s)\n- {2} lower letter(s)\n- {3} punctuation mark(s)\n- {4} space(s)".format(chars_len, upper_chars, lower_chars, puncs, spaces))


print(text_analyzer(sys.argv[1]))
