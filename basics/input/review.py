#For activity 5 i chose to create "Beep personal home asistant" O:) 

print("*******")
print("* o o *")
print("* --- *")
print("*******")
print("Hellow my name is Beep and i am your personal home asistant")
print("Can i ask for your name please")

name = input("Please enter your name:")

print(f"Nice to meet you {name}",)
print("I am here to support your house work")
print(" Please tell me what would you like me to do ?")
print("**************************************")
print("**   Beep home assistant funtions : **")
print("**   1 - Clean the house            **")
print("**   2 - Cook diner                 **")
print("**   3 - Take out the trash         **")
print("**   4 - Clean the cars             **")
print("**   5 - Exit                       **")
print("**************************************")
choice = int(input("Please select from option from 1 to 5 :  "))

if choice == 1:
   print("Im starting to clean the house!")
elif choice == 2:
   print("Im starting to cook diner!")
elif choice == 3:
   print("Im taking out the trash!")
elif choice == 4:
   print("Im starting to clean the cars!")
elif choice == 5:
  print("Thank good bye")
