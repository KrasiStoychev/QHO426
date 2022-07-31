#In the previous examples we used a for loop to retrieve a character in a string using its index position. This is useful when we wish to know the index number. However, in some cases we simply wish to retrieve the item from a list without tracking its position.

#In such scenarios we can use the for loop with membership operators such as the'in' and 'not' in operators.

#For example, let us assume we have a list of numbers assigned to a variable named number_list.  We can use a for loop and the in membership operator to iterate through each element as follows:

#for number in number_list:
    # do something     

# In class


# Ask user for phrase
print("What phrase do you see?")
phrase = input()

# Identify markings
print("\nReversing...\nThe phrase is : ", end="")

reversed = ""

for letter in phrase:
    reversed = letter + reversed

print(f":{reversed}") 