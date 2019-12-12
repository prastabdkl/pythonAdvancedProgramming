#WAP to plot the coordinates in a graph
#(0,0) (1,3) (2,1) (3,5)  (4,2)
import matplotlib.pyplot as plt

def main():
    x_cords = [0,1,2,3,4]
    y_cords = [0,3,1,5,2]

    plt.plot(x_cords,y_cords)
    plt.show()


main()
