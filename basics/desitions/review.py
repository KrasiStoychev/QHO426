print("************************************")
print("***** - National Bank - ************")
print("************************************")
print("************************************")
print("***** - List of services - *********")
print("***** 1 - chek total of accounts ***")
print("***** 2 - cash withdraw ************")
print("***** 3 - Cash deposite ************")
print("***** 4 - Send Money ***************")
print("***** 5 - Exit ***************")
print("************************************")
choice = int(input("Please select Service from 1 to 10: "))

if choice == 1:
   list = ["1","2","3","4","5","6","7","8","9","10"]
   list [0] = 250
   list [1] = 1250
   list [2] = 2503
   list [3] = 3503
   list [4] = 4503
   list [5] = 6503
   list [6] = 7503
   list [7] = 8503
   list [8] = 9503
   list [9] = 32503
   for i in range(10):
     a = ["1","2","3","4","5","6","7","8","9","10"]
    
     print(f" {a[i]} - {list[i]+1}")
     
   list_choice1 = int(input("select first  account that you would  like to add from 1 to 10 ? :"))
   if list_choice1 == 1:
      list_choice1 = 250
   elif list_choice1 ==2:
      list_choice1 = 1250
   elif list_choice1 ==3:
      list_choice1 = 2503
   elif list_choice1 ==4:
      list_choice1 = 3503
   elif list_choice1 ==5:
      list_choice1 = 4503
   elif list_choice1 ==6:
      list_choice1 = 6503
   elif list_choice1 ==7:
      list_choice1 = 7503
   elif list_choice1 ==8:
      list_choice1 = 8503
   elif list_choice1 ==9:
      list_choice1 = 9503
   elif list_choice1== 10:
      list_choice1 = 32503
   
   list_choice2 = int(input("select first  account that you would  like to add from 1 to 10 ? :"))
   if list_choice2 == 1:
      list_choice2 = 250
   elif list_choice2 ==2:
      list_choice2 = 1250
   elif list_choice2 ==3:
      list_choice2 = 2503
   elif list_choice2 ==4:
      list_choice2 = 3503
   elif list_choice2 ==5:
      list_choice2 = 4503
   elif list_choice2 ==6:
      list_choice2 = 6503
   elif list_choice2 ==7:
      list_choice2 = 7503
   elif list_choice2 ==8:
      list_choice2 = 8503
   elif list_choice2 ==9:
      list_choice2 = 9503
   elif list_choice2== 10:
      list_choice2 = 32503 
   result = list_choice1 + list_choice2
   print(result)
    

elif choice == 2: