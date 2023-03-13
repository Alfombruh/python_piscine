import re
from sys import argv

def text_analyzer(string):
    """This fucntions counts various characters inside a string"""
    print(f'- {sum(1 for c in string if c.isupper())} upper letters(s)')
    print(f'- {sum(1 for c in string if c.islower())} lower letters(s)')
    print(f'-',len(re.findall(r'[^\w\s]', string)),'punctuation mark(s)')
    print(f'- {sum(1 for c in string if c.isspace())} space(s)')

def main():
    if len(argv) != 2:
        return
    text_analyzer(argv[1])

if __name__ == "__main__":
    main()
