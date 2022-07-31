def directions():
    dirs = ["move forward","Move backward","turn left","Turn right"]
    return dirs

def menu():
    print("Please select direction")
    move = directions()
    for i in range(0 , len(move) , 1):
        print(f"{move[i]} is in index : {i}")

def run():
    menu()


run()