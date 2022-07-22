print("*****************************")
print("*** Beep Adventure picker****")
print("*****************************")
print("**** 1 - Safe adventure *****")
print("**** 2 - Long adventure *****")
print("**** 3 - Scary adventure ****")
print("**** 4 - short adventure ****")
print("")

adventure = int(input("what type of adventure would you like from 1 to 4 :"))

if (adventure == 1) or (adventure == 2):
   print("Entering the dark forest")

elif (adventure == 3) or (adventure == 4):
   print("Taking the safe route!")

