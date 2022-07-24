#Activity 2: Return Values (~ minutes)

#A function can return a value.  This is useful when we wish to return a result to a calling function (the caller) from a called function.  We can do this by using the keyword return.  For example, let us say we have a function that retrieves the name of a user.  Such a function may be coded as follows:
  
#def get_name():
  #print("Please enter your name")
  #name = input()
  #return name
  
#print("Retrieved name:", get_name())

#The above example the return keyword is used to return the value inputted by the user.  When a function returns a value, the original function call is replaced by the value returned by the called function.


##Task

###Bop is trying to distribute their weight so that both Beep and Bop can reach the top of the bridge ladder quicker. A program to help Bop achieve this consists of three functions as follows:

#The first function should be named sum_weights and should have 2 parameters. The parameters represent the weight of each bot. The function should calculate and return the total weight.

#The second function should be named calc_avg_weight and should also have 2 parameters. The parameters represent the weight of each bot. The function should calculate and return the average weight of the bots. It should do this by calling the first function and using the return value.

#The third function should be named run and should have 0 parameters. The function should prompt the user to enter the weight for each bot. The function should then prompt the user to enter either the word "sum" or "average". If the user types in "sum" then this function should display the total age as given by the first function ( sum_weights"). Otherwise if the user types in "average" then this function should display the average weight as given by the second function ( calc_avg_weight).

#The program should also contain a single call to your run function at the end of your program that looks as follows:

# Run the program
#run()




def sum_weights(beep_weight, bop_weight):
    total_weight = beep_weight + bop_weight
    return total_weight

def calc_avg_weight(beep_weight, bop_weight):
    avg_weight = (beep_weight + bop_weight) / 2
    return avg_weight

def run():
    # retrieve required user data
    print("What is the weight of Bop?")
    bop_weight = float(input())

    print("What is the weight of Beep?")
    beep_weight = float(input())

    print("What would you like to calculate (sum or average)?")
    action = input()

    # determine and carry out action
    if (action == "sum"):
        answer = sum_weights(beep_weight, bop_weight)
        print("The sum of Beep's and Bop's weight is {:.2f}".format(answer))
    elif (action == "average"):
        answer = calc_avg_weight(beep_weight, bop_weight)
        print("The average of Beep's and Bop's weight is {:.2f}".format(answer))
    else:
        print("I am not sure what you would like to do.")