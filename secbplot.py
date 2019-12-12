import matplotlib.pyplot as plt

def main():
    #(x,y) ={(0,0),(1,3),(2,1),(3,5),(4,2)} Given points

    x_coords = [0,1,2,3,4]
    y_coords = [0,3,1,5,2]
    #build a line graph
    plt.plot(x_coords,y_coords)

    plt.title('Sample Data')#adding title

    # Add labels to the axes.
    plt.xlabel('This is the X axis')
    plt.ylabel('This is the Y axis')
    
    plt.show()

main()
