from sys import argv
import sys
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
			'C':'-.-.', 'D':'-..', 'E':'.',
			'F':'..-.', 'G':'--.', 'H':'....',
			'I':'..', 'J':'.---', 'K':'-.-',
			'L':'.-..', 'M':'--', 'N':'-.',
			'O':'---', 'P':'.--.', 'Q':'--.-',
			'R':'.-.', 'S':'...', 'T':'-',
			'U':'..-', 'V':'...-', 'W':'.--',
			'X':'-..-', 'Y':'-.--', 'Z':'--..',
			'1':'.----', '2':'..---', '3':'...--',
			'4':'....-', '5':'.....', '6':'-....',
			'7':'--...', '8':'---..', '9':'----.',
			'0':'-----', ', ':'--..--', '.':'.-.-.-',
			'?':'..--..', '/':'-..-.', '-':'-....-',
			'(':'-.--.', ')':'-.--.-',' ':'/'}

if __name__ == "__main__":
	if len(argv) != 2:
		sys.exit("SO LONG KING BOWSER!")
	words = argv[1].split()
	for elem in words:
		for elem in elem:
			print(f'{MORSE_CODE_DICT[elem.upper()]}', end=" ")
		print("/", end="")
