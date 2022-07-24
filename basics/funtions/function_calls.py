##Beep and Bop wish to create a program which manipulate cryptic words. The program should prompt the user to enter a word. The program should then prompt the user to choose one of the following options:

#1) Display in a Box – display the word in an ascii art box
#2) Display Lower-case – display the word in lower-case e.g. hello
#3) Display Upper-case – display the word in upper-case e.g. HELLO
#4) Display Mirrored – display the word with its mirrored word e.g. Hello | olleH
#5) Repeat – ask the user how many times to display the word and then display the word that many times alternating between upper-case and lower-case.

#The program should then read the option number entered by the user and carry out the appropriate actions.

#The program should contain 6 user-defined functions. One for each of the above options and #one to run the program.

def display_box(word):
    num_dashes = 4 + len(word)
    print("-" * num_dashes)
    print("| {} |".format(word))
    print("-" * num_dashes)

def display_lower_case(word):
    print(word.lower())

def display_upper_case(word):
    print(word.upper())

def display_mirrored(word):
    mirrored = ""
    for letter in reversed(word):
        mirrored += letter
    print("{} | {}".format(word, mirrored))

def display_repeated(word):
    print("How many times should the word be displayed?")
    repetitions = int(input())

    for repetition in range(repetitions):
        # even repetition
        if (repetition % 2 == 0):
            print(display_lower_case(word))
        # odd repetition
        else:
            print(display_upper_case(word))

def run():
    print("Please enter a word:")
    word = input()

    # remember the user has not yet selected an option
    response = 0

    while (response != 6):
        # get the user's selection
        print("What would you like to do with this word?")
        print("[1] Display in a box")
        print("[2] Display lower-case")
        print("[3] Display upper-case")
        print("[4] Display mirrored")
        print("[5] Display repeated")
        print("[6] Quit")

        response = int(input()) 
 
        # determine and execute action
        if (response == 1):
            display_box(word)
        elif (response == 2):
            display_lower_case(word)
        elif (response == 3):
            display_upper_case(word)
        elif (response == 4):
            display_mirrored(word)
        elif (response == 5):
            display_repeated(word)
        elif (response == 6):
            break
        else:
            print("Unknown option.") 

run()