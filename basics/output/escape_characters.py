#We have thus far learnt that the print function can be used to output text to the screen. Often, we would like to have more control over how text is displayed. There are a number of ways to do this but one approach is to use special character sequences known as escape characters. These sequences consist of two or more characters and begin with a back slash (\).
## Display escape characters
#print("\n Displays a new line")
#print("\t Displays a tab space")
#print("\\ Displays a back slash")
#print("\" Displays a double quote")
#print("\' Displays a single quote")

print("\n Displays a new line")
print("\t print a tab")
print("\\ print a back slash")
print("krasi said \"hello\"")
print()
print('              "I am Beep"     ')
print()
print("##########")
print("#        #")
print("#        #")
print("##########")

#A back slash followed by the character n i.e. \n indicates that the output should move to a new line before displaying the next sequence of characters. Similarly, \t will cause a tab space to be displayed.

#What if we wish to display a back slash? Since a back slash indicates the start of an escape character sequence we would need to use \\ when we wish to display an actual back slash.

#The escape characters \" and \' are useful when we wish to display a double quote or a single quote. This helps us overcome the problem where we wish to display quotes inside a string that begins with double or single quotes.

