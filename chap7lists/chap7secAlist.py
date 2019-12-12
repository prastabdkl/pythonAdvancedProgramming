import random
list1 = []
for count in range(5):
    list1.append(random.randrange(1,100))
#print(list1)

numbers  = list(range(11))
print(numbers)
numbers  = list(range(1,5))
#print(numbers)
numbers  = list(range(1,10,3))
#print(numbers)
numbers  = list(range(11))
""" print(numbers[1:5])
print(numbers[5:])
print(numbers[:9])
print(numbers[:]) """
""" search_key = int(input('Enter the value to search'))
if search_key not in numbers:
    print('The element does notexists')
else:
    print('Element not found is not true')
 """
##### tuple
my_tuple =(33,22,11)
#print(my_tuple)
#my_tuple.sort() operations like sort,reverse,append,extend,delete are not possible
# because a tuple is immutable

#conversion between list and tuple
my_new_tuple =(10,20,30)
print(my_new_tuple)
new_list =list(my_new_tuple)
print(new_list)

list1 = ['Ram','Shyam','Hari']
print(list1)
new_tuple = tuple(list1)
print(new_tuple)