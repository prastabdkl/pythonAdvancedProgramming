# plotting a Piechart
# Author: Prastab Dhakal
# Chapter: plotting

import matplotlib.pyplot as plt


def main():
    #create a list of values
    values=[20,60,80,40]
    
    #title
    plt.title("PIE CHART")
    
    #create a list of labels for the slices.
    slice_labels=['1st Qtr','2nd Qtr','3rd Qtr','4th Qtr']
    
    
    #create a pie chart from the values
    plt.pie(values,labels=slice_labels,colors=('r','b','y','c'))
    
    
    #display the pie chart.
    plt.show()

#defining main function
main()