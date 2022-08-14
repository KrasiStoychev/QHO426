import matplotlib.pyplot as plt


def coordinate():
     x = []
     user_x = int(input("Please Enter value for x : "))
     user_y = int(input("Please Enter value for y : "))
     return (user_x, user_y)

def path():
    data = coordinates()
    print("Retrieving path...")
    x_values = []
    y_values = []
    for i in range(4):
    
    x_values.apped(data[0])
    y_values.apped(data[1])
    return (x_value, y_values)

def run():
    values = path()
    plt.plot(values[0],values[1], "ro--")
    plt.xlable("X values")
    plt.ylable("Y values")
    plt.show()

run()