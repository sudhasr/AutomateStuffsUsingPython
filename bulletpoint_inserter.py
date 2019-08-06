#! python3

"""Adds Wikipedia bullet points to the start
of each line of text on the clipboard."""

import pyperclip

#Paste text form the clipboard
text = pyperclip.paste()

#split the text into separate lines
lines = text.split('\n')

for i in range(len(lines)):    
    lines[i] = '* ' + lines[i] #Add * tot he start of each line. Here star symbol os the bullet

text = '\n'.join(lines) #join the lines into a single text

#copy to clipboard
pyperclip.copy(text)