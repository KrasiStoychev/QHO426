print("****************")
print("**Book Covers***")
print("****************")
cover_type = input("Please select cover type: hard or soft:")
if cover_type == 'soft':
   perfect_bound = input("Is your Book perfect bond : Select Yes or No : ")
   if perfect_bound == 'yes':
      print("soft cover, perfect bound book are very popular! ")

   else:
     print("Soft covers with coils or stitches are great for short books")

else:
  print("Books with hard covers can be more expensive!")
  