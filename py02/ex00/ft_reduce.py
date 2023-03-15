def ft_reduce(function, value, initializer = None):
	iterator = iter(value)
	if initializer is None:
		initializer = next(iterator)
	sum = initializer
	for elem in iterator:
		sum = function(sum, elem)
	return sum

# def add(x, y):
# 	return x + y

# var = [1, 2, 3, 4, 5]
# print(var)
# print(ft_reduce(add, var))