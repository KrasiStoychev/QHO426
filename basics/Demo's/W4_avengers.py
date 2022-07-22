def adding(lista = []):
    new_member = input("Enter new avenger : ")
    lista.append(new_member)

def removing(lista = []):
    rejected = input("Enter avenger to be removed : ")
    if rejected in lista:
       lista.remove(rejected)


def printing(lista = []):
    for hero in lista:
      print(f"The mighty {hero} is part of avengers!")


def run():
    avengers = []
    while True:
      opt = int(input("Avengers Asemble\n\n1-Add a new avenger\n\n2-Remove avenger\n\n3-Check on the team\n\n9-Exit\n\nPlease make your choice : "))
      if opt == 1:
         adding(avengers)
      elif opt == 2:
        removing(avengers)
      elif opt == 3:
           printing(avengers)
      elif opt == 9:
           break
      else:
        print("No such thing exists.Try agen!")
   
run()