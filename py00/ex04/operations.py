from sys import argv
import sys

def sum(A, B):
    return A + B

def diff(A, B):
    return A - B

def prod(A, B):
    return A * B

def quo(A, B):
    return A / B

def rem(A, B):
    return A % B

def main():
    if len(argv) > 3:
        sys.exit('AssertionError: too many arguments')
    if len(argv) < 3:
        sys.exit('Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3')
    try:
        i = int (argv[1])
        j = int (argv[2])
    except:
        sys.exit('AssertionError: only integers')
    print(f'Sum:        {sum(i, j)}')
    print(f'Difference: {diff(i, j)}')
    print(f'Product:    {prod(i, j)}')
    if j == 0:
        print('Quotient:   ERROR (Division by zero)')
    else:
        print(f'Quotient:   {quo(i, j)}')
    if j == 0:
        print('Remainder:  ERROR (modulo by zero)')
    else:
        print(f'Remainder:  {rem(i, j)}')

if __name__ == "__main__":
    main()
