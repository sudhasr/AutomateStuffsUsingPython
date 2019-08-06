#! python3

"""MapIt.py - Program to launch the Google maps based on the location
given as command line arguments or taken from the clipboard"""

#importing the webbrowser module for launching the browser
#importing sys module for taking the command line arguments
#importing pyperclip which is a clipboard module
import webbrowser, sys, pyperclip

if len(sys.argv) == 1:
	#Get address from clipboard
	address = pyperclip.paste()
	
elif len(sys.argv) < 4:
	print("Please enter the full address")
	
else:
	#Get address from command line 
	address = " ".join(sys.argv[1:])
	webbrowser.open('https://www.google.com/maps/place/' + address)
