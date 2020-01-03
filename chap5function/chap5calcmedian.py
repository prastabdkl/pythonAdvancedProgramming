# A program that calculates median of numbers in a list
# Author: Prastab Dhakal
# Chapter: functions
import math
def get_input():
    new_list = []
    number_of_terms = int(input('Enter the number of terms'))
    for count in range(0,number_of_terms):
        new_list.append(int(input('Enter the element')))

    return number_of_terms,new_list

def calculate_median(list1,N):
    list1.sort()
    position = (N+1)/2
    if(N%2==0):
        lower_term = list1[(math.floor(position))-1]
        upper_term = list1[(math.ceil(position))-1]
        median = (lower_term+upper_term)/2
        return median
    else:
        return list1[int(position-1)]
        # print('The median is ', list1[int(position-1)])

def main():
    number_of_terms,list1 = get_input()
    #print(number_of_terms,list1)
    median = calculate_median(list1,number_of_terms)
    print(median)

main()