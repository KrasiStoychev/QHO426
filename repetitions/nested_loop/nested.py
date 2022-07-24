#Loops can be nested.  That is one loop can be placed inside another.  When this is done it results in the inner loop being executed for each iteration of the outer loop.


#[Explanation]

#Let us consider a simple example where we wish to display the digits 0-9 on a single line. We can do this using a single loop as follows:

#for number in range(0, 10, 1):
    #print(number, "|", end="")

#The above code will result in the following output where the line of digits is repeat 3 times one after the other:

#0 |1 |2 |3 |4 |5 |6 |7 |8 |9 |

#Note, that all the numbers are displaying on the same line. This is because we have overridden the default behaviour of the print function. By default the print function adds a new line (\n) to the end of a line. However, by using end="" we have specified that an empty string ("") should be added to the end of the printed line instead of a new line (\n).

#Now let us assume we wish to display the previous line of digits 3 times. Effectively, we wish to repeat the previous loop three times. We can do this placing our existing loop inside #another loop that repeats 3 times as follows:

#for count in range(0, 3, 1):
    #for number in range(0, 10, 1):
        #print(number, "|", end="")
#The above code will result in the following output:

#0 |1 |2 |3 |4 |5 |6 |7 |8 |9 |0 |1 |2 |3 |4 |5 |6 |7 |8 |9 |0 |1 |2 |3 |4 |5 |6 |7 |8 |9 |
#Note that all the numbers are displayed on the same line as we have not included an instruction in the program to display to the next line. Assume our intention was to display each set of digits on a new line. This means on each iteration of the outer loop we will need to move to a new line. Our code would therefore look as follows:
#for count in range(0, 3, 1):
    #for number in range(0, 10, 1):
        #print(number, "|", end="")
    #print()
#The above code will result in the following output:

#0 |1 |2 |3 |4 |5 |6 |7 |8 |9 |0 |1 |2 |3 |4 |5 |6 |7 |8 |9 |0 |1 |2 |3 |4 |5 |6 |7 |8 |9 |
#Note that all the numbers are displayed on the same line as we have not included an instruction in the program to display to the next line. Assume our intention was to display each set of digits on a new line. This means on each iteration of the outer loop we will need to move to a new line. Our code would therefore look as follows:
#for count in range(0, 3, 1):
    #for number in range(0, 10, 1):
        #print(number, "|", end="")
 #-   #print 

#We can visualise the code as follows:

#nested loop


#In the above code, the last print statement will cause a new line (\n) character to be #displayed after the inner loop has completed execution. The resulting output would look as #follows:

#0 |1 |2 |3 |4 |5 |6 |7 |8 |9 | = print() to print a new line
#0 |1 |2 |3 |4 |5 |6 |7 |8 |9 |
#0 |1 |2 |3 |4 |5 |6 |7 |8 |9 |

#In class

# Ask user for columns and rows
print("How many rows should I have?")
rows = int(input())

print("How many columns should I have?")
columns = int(input())

# Display grid
for row in range(0, rows, 1):
    for column in range(0, columns, 1):
        print(":-)", end="")
    print()
