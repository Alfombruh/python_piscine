import sys
from sys import argv
from string import punctuation


def findPunctuation(string):
    for elem in punctuation:
        if string.find(elem) == -1:
            return -1
    return 0

if (__name__ == "__main__"):
    if len(argv) != 3:
        sys.exit("ERROR")
    try:
        wordCount = int(argv[2])
    except ValueError:
        sys.exit("ERROR")
    words = argv[1].split()
    print('[', end="")
    for elem in words:
        if len(elem) > wordCount and findPunctuation(elem) == -1:
            print (f"'{elem}'", end = ', ')
    print(']')