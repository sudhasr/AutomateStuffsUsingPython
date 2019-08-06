#! python3

"""If no arguments passed to strip() then remove 
whitespaces from beginning and end. Otherwise 
characters specified as second argument in 
strip() will be removed from the string"""

import re

some_string = input("Enter the string")

some_char  = input("Enter the character")

def regex_strip(some_string,some_char):

	a = re.compile(r'[%s]'%(some_char))
	return a.sub('',some_string)

print (regex_strip(some_string,some_char))