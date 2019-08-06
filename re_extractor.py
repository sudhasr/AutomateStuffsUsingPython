#! python3

"""Program to extract e-mail and phone number using regex"""

import pyperclip
import re

a_text = str(pyperclip.paste()) #This a_text contains the email and phonenumber

#Creating patterns for phone number and e-mail
phonenumber_pattern = re.compile(r'''(
	(\d{3}|\(\d{3}\))?    # Non greedy approach for area code
	(\s|-|\.)?            # hypen or a dot (Phone number format) 
	(\d{3})               # first 3 digit
	(\s|-|\.)?            # seperator
	(\d{4})               # Last 4 digit
	)''', re.VERBOSE)

email_pattern = re.compile(r'''(
	[a-zA-Z0-9._%+-]+      # Username
	@                      # symbol
	[a-zA-Z0-9.-]+         # domain name
	(\.[a-z{2,4}])         # dot-something
	)''', re.VERBOSE)


# list that will contain all the matches
matches =[] 

for groups in phonenumber_pattern.findall(a_text):
	phone_number = '-'.join([groups[1],groups[3],groups[5]])
	matches.append(phone_number)

for groups in email_pattern.findall(a_text):
	matches.append(groups[0])

# Copy results to clipboard

if len(match) > 0:
	pyperclip.copy('\n'.join(matches))
	print ('MAtches Copied to clipboard')
	print ('\n'.join(matches))
else:
	print ('Match Not Found')