from sys import argv

def reverseSwapCaseString(string):
    return string[::-1].swapcase()


def main():
    if len(argv) < 2:
        return
    string = ' '.join(argv[1::])
    print(reverseSwapCaseString(string), end = "")

if __name__ == "__main__":
    main()
