import matplotlib.pyplot as plt


def small():
    x = [3, 3, 4, 4, 3]
    y = [3, 4, 4, 3, 3]

    plt.plot(x, y, 'ro--')



def medium():
    x = [2, 2, 5, 5, 2]
    y = [2, 5, 5, 2, 2]

    plt.plot(x, y, 'bo--')



def lardge():
    x = [1, 1, 6, 6, 1]
    y = [1, 6, 6, 1, 1]

    plt.plot(x, y, "gx--")


def run():
    small()
    medium()
    lardge()
    plt.show()

run()