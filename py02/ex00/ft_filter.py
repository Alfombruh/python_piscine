def ft_filter(function, list):
	return [x for x in list if function(x)] #returns a new list node with x if x is in the list when function(x) returns tru

# def isEven(x):
# 	return x % 2 == 0

# list = [0, 1, 2, 3, 4, 5, 6, 7 , 8, 9]
# print(list)
# print(ft_filter(isEven, list))