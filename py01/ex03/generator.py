import random

def rShuffle(text):
	for i in range(len(text) - 1, 0, -1):
		j = random.randint(0, i)
		text[i], text[j] = text[j], text[i]
	return text

def generator(text, sep = " ", option=None):
	'''Divides the text according tto the value of sep and will produce sub_strings
		options specifices if an action will happen on the substring before being produced
		Options: "shuffle, unique, ordered"
	'''
	newText = text.split()
	if option == 'shuffle':
		newText = rShuffle(newText)
	if option == 'unique':
		newText = list(set(newText))
	if option == 'ordered':
		newText.sort()
	for elem in newText:
		yield elem

# if __name__ == "__main__":
# 	text = "Le Lorem Ipsum est simplement du faux texte"
# 	print('Right Order\n\n')
# 	for word in generator(text, sep=" "):
# 		print(word)
# 	print('\nRandom Shuffle\n')
# 	for word in generator(text, sep=" ", option='shuffle'):
# 		print(word)
# 	print('\nOrdered\n')
# 	for word in generator(text, sep=" ", option='ordered'):
# 		print(word)
# 	print('\nUnique\n')
# 	for word in generator(text, sep=" ", option='unique'):
# 		print(word)