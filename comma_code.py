#! python3

"""Write a function that takes a list value as an argument 
and returns a string with all the items separated by a comma 
and a space, with 'and' inserted before the last item. 
But your function should be able to work with any list 
value passed to it."""


def comma_code(a):
	result = ''
	last_item = spam[len(spam)-1]
	last = 'and '+last_item
	spam[len(spam)-1] = last
	
	result = ', '.join(spam)
	print(result)

spam = ['apples', 'banana', 'orange', 'kiwi']
comma_code(spam)	