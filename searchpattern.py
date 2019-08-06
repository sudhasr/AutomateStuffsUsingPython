#! python3 

"""Traversing all the .txt files in a folder
and searching for any line that matches regex
Print the result"""

import os
import re

# Open the file
file_open = open(filename,'r')

try:
	# Get pattern from user
	regex_in = input("Enter the regular expression")

	# search initially 
	match = re.search(regex_in,filename)

	# If Regular expression search successful
	if match!=None:

		# Make a complete search throughout the whole file
		match_all = re.findall(regex_in,filename)

        # Print the result
		print "Result:" + str(match_all)

except IOError as e:
	print ("File requested doesn't exist. Try again!")


file_open.close()
