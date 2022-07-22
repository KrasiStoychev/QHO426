def moovments():
    return ["Move forward",10,"mova backword",5,"Move left",3,"Move right",1]
            
def run():
    print("Moving")
    micky_mouse = moovments()
    for i in range(0 , len(micky_mouse) , 2):
          print(f"{micky_mouse[i]} for {micky_mouse[i+]} steps")

run()
