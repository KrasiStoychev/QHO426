#We can iterate through a list using indexes and a loop in any direction. If, for example, we wish to iterate through a list in reverse then we can start with the largest index (the length of a word - 1) and work our way down to 0 which is the index of the first character.


# Ask user for phrase
print("What phrase do you see?")
phrase = input()

# Identify markings
print("\nReversing...\nThe phrase is", end="")

for position in range(len(phrase) - 1, -1, -1):
    print(phrase[position], end="")