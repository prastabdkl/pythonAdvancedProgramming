""" WAP to generate a list of 30 random numbers, 
sort the list, convert the list to tuple, 
store the following elements in the list:
	 1,2,3 element,
	 10 to 20,
	 and last 3 elements 
 and find the sum of these elements """
 
import random
def get_input():
    random_list = []
    for count in range(30):
        a = random.randrange(1,100)
        random_list.append(a)
    return random_list

def slicing_function(new_tuple):
    #print(new_tuple)
    #print('First 3 elements',new_tuple[:3])
    #print('10 to 20 elements', new_tuple[9:20])
    #print('last 3 elements',new_tuple[-3:])
    new_list = []
    my_tuple = new_tuple[:3] + new_tuple[9:20] + new_tuple[-3:]
    new_list = list(my_tuple)
    print('The list after adding the elements is',new_list)
    total = 0
    for element in new_list:
        total += element
    return total
    #return sum(new_list)

def main():
    random_list = get_input() #taking the input
    print('The random list is',random_list)
    random_list.sort() #sort
    print('The list after sorting is',random_list)
    new_tuple = tuple(random_list) #list to tuple conversion
    total_sum = slicing_function(new_tuple)
    print('The total sum is',total_sum)
main()