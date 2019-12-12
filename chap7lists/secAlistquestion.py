import random
def get_input():
    random_list = []
    for count in range(30):
        a = random.randrange(2,200)
        random_list.append(a)
    return random_list
def slicing_function(my_tuple):
    """ print(my_tuple[:3])
    print(my_tuple[9:19])
    print(my_tuple[27:])
    print(my_tuple[-3:]) """
    print()
    """ list1 = list(my_tuple[:3])
    list2 = list(my_tuple[9:19])
    list3 = list(my_tuple[-3:])
    list4 =[]
    list4.extend(list1)
    list4.extend(list2)
    list4.extend(list3)
    print(list4) """
    new_tuple = my_tuple[:3] + my_tuple[9:19] + my_tuple[-3:]
    print(new_tuple)
    new_list = list(new_tuple)
    print(new_list)

    #sum
    total = 0
    for element in new_list:
        total += element
    print(total)

    #next method for sum
    total = sum(new_list)
    print(total)
    
def main():
    random_list = get_input()
    print('unsorted:',random_list)
    random_list.sort()
    print('Sorted:',random_list)
    my_tuple = tuple(random_list)
    print(my_tuple)
    slicing_function(my_tuple)

main()