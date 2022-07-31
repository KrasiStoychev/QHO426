def interests():
    print("Enter all your interests one after the other and enter \"stop\" when done")
    s1 = set()
    while True:
         interest = input()
         if interest.lower() == 'stop':
             break
         else:
            s1.add(interest)
    return s1

def tinderdasecond():
    print("first person")
    p1 = interests()
    print("Second person")
    p2 = interests()
    common = p1.intersection(p2)
    if len(common) >= 3:
       print(f"Yay - you are a match made in haven! You have {len(common)} common interests")
    else:
      print("Oh no there is now way that it will work out :(")


tinderdasecond()