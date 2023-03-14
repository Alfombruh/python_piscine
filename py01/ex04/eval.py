import sys

class Evaluator:
	def zip_evaluate(coefs, words):
		if len(coefs) != len(words):
			sys.exit("-1")
		tot = 0
		for i, j in zip(words, coefs):
			tot += len(i) * j
		print(tot)

	def enumerate_evaluate(coefs, words):
		if len(coefs) != len(words):
			sys.exit("-1")
		tot = 0
		for index, text in enumerate(words):
			tot += len(text) * coefs[index]
		print(tot)


if __name__ == "__main__":
	words = ["Le", "Lorem", "Ipsum", "est", "simple"]
	coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
	Evaluator.zip_evaluate(coefs, words)

	# words = ["Le", "Lorem", "Ipsum", "n'", "est", "pas", "simple"]
	# coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42, 33]
	Evaluator.enumerate_evaluate(coefs, words)
