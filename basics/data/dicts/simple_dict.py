#We can create a dictionary in python using curly braces {} or the function dict().  For example, if we wish to create a dictionary representing items at wedding then we can do this as follows:

#wedding = {}

#We can create and initialise our dictionary with some elements by providing these between the curly brackets:

#wedding = {"Cake":1, "Car":1, "Ribbons":100}

#Alternatively, we can create an empty list ann add elements later:

#wedding = {}
#wedding["Cake"] = 1
#wedding["Car"] = 1
#wedding["Ribbons"] = 100
#[Tasks]

#We wish to create a program to help Beep and Bop decipher the pattern.
#The program should consist of the following two functions:

#The first function should be named pattern and should have no parameters.
#The function should create a dictionary named sequences.
#The function should populate the dictionary with the following items: "Short Sequence":3, #"Medium Sequence":2, "Long Sequence":1
#Finally, the function should return the dictionary
#The second function should be named run and should have no parameters. 
#The function should call the first function and display the dictionary returned by the call.

#An example run of such a program is shown below:

#{'Short Sequence':3, 'Medium Sequence':2, 'Long Sequence':1}

#Start by creating a new python file simple_dict.py and store the file in the following location:

#data/dicts/simple_dict.py

def pattern():
  sequences = {"Short Sequence":3, "Medium Sequence":2, "Long Sequence":1}
  return sequences

def run():
  print(pattern())

run()