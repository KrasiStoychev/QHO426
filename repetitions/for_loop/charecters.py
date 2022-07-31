#One common use of loops is with strings. A string, in Python, is a list of characters. That is, it consists of many characters that are ordered. We can use indexing to get an element in a list where the first element in a list is at position 0, the second character at position 1 and so on. So, to retrieve the first character in a string we can do the following:
#user_string[0]

#Where user_string is variable of data type string and the number 0 is the index number of the first character in the string.

#A loop can be used to iterate through each character in a string. For example, let us assume we wish to display each character in a string entered by a user. We could do the following:

#print("Please enter a word")
#user_word = input()

#for position in range(0, len(user_word), 1):
    #print(user_word[position])

#In the above code a for loop is used to iterate through a range of numbers from 0 up to, but not including, the length of user_word. These numbers represent the position of each of the characters in the word. Hence, the position is used to index and display a character in user_word with the first character at an index of 0.
#Although the above is a simple example it demonstrates how useful loops can be particularly when used with strings or other data structures.

#INCLASS

# Ask user for markings
print("What strange markings do you see?")
markings = input()

# Identify markings
print("Identifying...")

for count in range(0, len(markings), 1):
    print(f"index {count} : {markings[count]}")
  
