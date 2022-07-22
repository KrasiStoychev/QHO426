#start with 2 counters that store the result of cheking each number slot after taking user input
even =0
odd =0


#asking for the input then cheking if the number is even or odd add one to the count of the varuable of each group
number_1 = int(input("Please enter first number : "))
rem = number_1 % 2
if (rem ==0):
   even = even + 1
else:
   odd = odd + 1


number_2 = int(input("Please enter second number : "))
rem = number_2 % 2
if (rem ==0):
   even = even + 1
else:
   odd = odd + 1


number_3 = int(input("Please enter tird number : "))
rem = number_3 % 2
if (rem ==0):
   even = even + 1
else:
   odd = odd + 1

print(f" There where {even} even numbers and {odd} numbers")