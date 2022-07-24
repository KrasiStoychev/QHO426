#We wish to create a program to help Beep and Bop climb the bridge ladder.

#The program should start by defining a function that has the name climb_ladder and which takes 2 parameters representing the number of steps remaining and the number of steps crossed.
#The function should do the following:
    #Compare the values of the two parameters such that if the number of steps remaining is #greater than the number of steps crossed then the message "Still some way to go!" should be displayed.
    #Otherwise the message "We are almost there!" should be displayed.
#Finally, the program should contain the following calls to your climb_ladder function:



def climb_ladder(steps_remaining, steps_crossed):
    # Compare and display a suitable message
    if (steps_remaining > steps_crossed):
        print("Still some way to go!")
    else:
        print("We are almost there!") 


climb_ladder(5, 2)
climb_ladder(2, 5)
