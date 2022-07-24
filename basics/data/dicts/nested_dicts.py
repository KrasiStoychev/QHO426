#We can also create a dictionary of dictionaries as shown below:

#wedding = {
    #"items":{"Cake":1, "Car":1, "Ribbons":100},
    #"people":{"guests":30}
#}
#We can also iterate through the dictionary using the method items and a suitable for loop:
#for key, value in wedding.items():
    #print(f"{key}: {value}")

#[Tasks]

#We wish to create a program to help Beep and Bop identify the patterns.

#The program should consist of the following four functions:
#The first function should be named short_pattern and should have no parameters.
#The function should create a dictionary named pattern.
#The function should populate the dictionary with the following key-value pairs:
#"sequence":"101"
#"occurrences":5
#Finally, the function should return the dictionary.

#The second function should be named medium_pattern and should have no parameters.
#The function should create a dictionary named pattern.
#The function should populate the dictionary with the following key-value pairs:
#"sequence":"111000"
#"occurrences": 25
#Finally, the function should return the dictionary

#The third function should be named long_pattern and should have no parameters.
#The function should create a dictionary named pattern.
#The function should populate the dictionary with the following key-value pairs:
#"sequence":"1100110011001100"
#"occurrences":50
#The fourth function should be named run and should have no parameters.
#The function should start by displaying the message "Analysing patterns...".
##The function should then create a dictionary with the following key-value pairs:
#"short sequence": value returned from first function
#"medium sequence": value returned from second function
#"long sequence": value returned from third function
#Finally, the function should display the content of the dictionary as key-value pairs using an appropriate loop

#An example run of such a program is shown below:

#Analysing patterns...
#short sequence: {'sequence': '101', 'occurrences': 5}
#medium sequence: {'sequence': '111000', 'occurrences': 25}
#long sequence: {'sequence': '1100110011001100', 'occurrences': 50}
#Start by creating a new python file nested_dicts.py and store the file in the following #location:

#data/dicts/nested_dicts.py
#Code your solution and be sure to include appropriate comments in your code.

def short_pattern():
  pattern = {"sequence":"101", "occurrences":5}
  return pattern

def medium_pattern():
  pattern = {"sequence":"111000", "occurrences":25}
  return pattern

def long_pattern():
  pattern = {"sequence":"1100110011001100", "occurrences":50}
  return pattern

def run():
  print("Analysing patterns...")
  patterns = {
    "short sequence":short_pattern(),
    "medium sequence":medium_pattern(),
    "long sequence":long_pattern()
  }
  
  for key, value in patterns.items():
    print(f"{key}: {value}")

run()