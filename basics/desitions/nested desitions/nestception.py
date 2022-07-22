print("Where should i look?")
print("1 - in the bedroom")
print("2 - in the bathroom")
print("3 - in the lab")
room = input("Please Enter a location")

if room == 'in the bedroom':
   print("Where in the bedroom should i look")
   print("under the bed or somewhere else?  ")
   where_to_go = input("Select 'under the bed' or 'somewhere else'  :")
   if where_to_go == 'under the bed':
      print("Found some shoes but no battery")
   else:
     print("Found some mess but no battery")

elif room == 'in the bathroom':
  print("Where in the bathroom should i look")
  print("in the bathtub or somewhere else?  ")
  where_to_go = input("Select 'bathtub' or 'somewhere else'  :")
  if where_to_go == 'under the bed':
      print("Found a rubber duck but no battery")
  else:
     print("Found a wet surface but no battery")

elif room == 'in the lab':
  print("Where in the lab should i look")
  print("on the table or somewhere else?  ")
  where_to_go = input("Select 'on the table' or 'somewhere else'  :")
  if where_to_go == 'on the table':
      print("Yes! I found my battery!")
  else:
     print("Found some tools but no battery.")
     
   
  