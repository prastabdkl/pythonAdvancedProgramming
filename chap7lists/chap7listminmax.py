# A program to find the greatest and smallest in a list 
# 
# Author: Prastab Dhakal
# Chapter: Lists

""" list1 = [15,10,25,17,13]
new_list1 = []
 for i in range(0,len(list1)):
    print(new_list1[i])
print()
for i in range(5):
    print(list1[i])
 """
def greatest_smallest(arr):
    arr.sort()
    print('Greatest element is:',arr[0])
    print('Greatest element is:',arr[-1])
    
def calculate_greatest(arr):
    max= arr[0]
    #loop through the list1
    for i in range(1,len(arr)):
        #compare elements of list1 with max
        if (arr[i] > max):
            max = arr[i]
    print('Greatest element is:',max)

def main():
    new_list1 = []
    for i in range(5):
        new_list1.append(int(input('Enter an Integer list1')))
    calculate_greatest(new_list1)

    for i in range(0,len(new_list1)):
        print(new_list1[i])
        
main()
