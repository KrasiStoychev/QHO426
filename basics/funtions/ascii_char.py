#Show that program have started
print("Program Started!")
#take user input and tore it 
print("Please enter an ASCII code:")
code = int(input())
#check user input and print results
if (code >= 32 and code <= 126):
    print("The character represented by the ASCII value {} is: {}".format(code, chr(code)))
else:
    print("The character cannot be displayed.")
#show that the program ended
print("Program Ended!")
