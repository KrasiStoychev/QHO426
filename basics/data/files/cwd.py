#It is often useful to check our current working directory before beginning to work with files so that we can provide appropriate file paths.  We can do this using the method getcwd of the module oswhich displays the file path of the current working directory.
#import os
#path = os.getcwd()
#print(f"Current Working Directory: {path}")

#We can also display the content of this directory using the method listdir of the module os as follows:

#for file in os.listdir(path):
  #print(file)

#[Tasks]

#We wish to create a program to display information about the current working directory.

#The program should consist of the following two functions:

#The first function should be named cwd and should have no parameters.
#The function should retrieve the file path for the current working folder.
#The function should then display the message "The current working directory is {path}" where #{path} is the previously retrieved path.
#The function should then display the message "The directory contains the following:".
#Finally, the function should display each file contained in the current working directory.
#The second function should be named run and should have no parameters. 
##The function should display the message "Processing...".
#The function should then call the first function.

#An example run of such a program is shown below:

#Processing...
#The current working directory is /home/runner/com411
##The directory contains the following:
#LICENSE
#basics
#data
#main.py

#Start by creating a new python file cwd.py and store the file in the following location:

#data/files/cwd.py


import os

def cwd():
  path = os.getcwd()
  print(f"The current working directory is {path}")
  print(f"The directory contains the following:")
  for file in os.listdir(path):
    print(file)

def run():
  print("Processing...")
  cwd()
