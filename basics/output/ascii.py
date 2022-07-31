#We can be creative in our use of the print function so as to produce more interesting output. For example, we can use the print function to create ascii art, that is, pictures composed of printable characters. For example, let us say we wish to display a box. We may do this by 
#display strings consisting of hash (#) characters and spaces as shown below:


# Display an ASCII art robot
print("##########")
print("#  o  o  #")
print("#  ----  #")
print("##########")

print("Please enter charecter for the eyes ?")
eyes = input()
print("##########")
print(f"#  {eyes}  {eyes}  #")
print("#  ----  #")
print("##########")



# Display an ASCII art robot using a long string
print(""" 
##########
#  o  o  #
#  ----  #
##########
""")