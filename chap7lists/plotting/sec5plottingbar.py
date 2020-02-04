# plotting a Piechart
# Author: Prastab Dhakal
# Chapter: plotting

import matplotlib.pyplot as plt

###barchart
def main():
    #create a list with the X coordinates of each bar's left edge.
    left_edges=[0,10,20,30,40]
    
    #create a list with the heights of each bar.
    heights=[100,200,300,400,500]
    
    #create a avariable fot the bar witdh
    bar_width=5
    
    #color for bar
    
    
    #Build the bar char.
    plt.bar(left_edges,heights,bar_width,color=('r','g','b','y','k'))
    
    #set the axis limit
    plt.xlim(xmin=-1,xmax=45)
    plt.ylim(ymin=-1,ymax=500)
    
    #Add a title
    plt.title("Sales by Year")
    
    #Add labels to the axes.
    plt.xlabel("Year")
    plt.ylabel("Sales")
    
    
    #customize the tick marks.
    plt.xticks([0,10,20,30,40],['2016','2017','2018','2019','2020'])
    plt.yticks([100,200,300,400,500],['$1m','$2m','$3m','$4m','$5m'])
    #Display the bar chart
    plt.show()
    
#call the main function
main()