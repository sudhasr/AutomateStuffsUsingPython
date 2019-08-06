#! python3

"""Program to detect password strength"""

import re

def strong_pass(Password):

	
	if re.match(r'([a-zA-Z0-9]).{8,}', Password) is not None:
		print ('Strong Password')
	else:
		print ('Weak Password')

pwd = "abracadaRAA@321"
strong_pass(pwd)

