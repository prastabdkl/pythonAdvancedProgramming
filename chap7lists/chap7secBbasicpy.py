numbers = list(range(5))
#print(numbers) #this creates ...

numbers = list(range(1,5))
#print(numbers)

numbers = list(range(1,10,2))
#print(numbers)

numbers =[1,2] * 3
#print(numbers)

numbers = list(range(1,10)) #1,2,3,4,5,6,7,8,9
#print(numbers)
#print(numbers[1:5])
#print(numbers[2:])
#print(numbers[:3])
#print(numbers[:])
#print(numbers[0:10:2])
#print(numbers[-4:])
""" 
search = int(input('Enter the element you want to search'))
if search not in numbers:
    print('The number was notfound in the list ')
else:
    print('The number was  found in the list')
 """
list1 = [3,2,1]
list2 = [3,4,5]
list3 = list1+list2
#print(list3)
days_of_week = ['Sun','Mon','Tues','Wed','Thurs','Fri','Sat']
mid_day =days_of_week[2:5]
#print(mid_day)

#### tuple.....
my_tuple = (1,2,3,4,5)
#print(my_tuple)
#print(my_tuple[1:3])
#print(list1.sort())
#my_tuple.sort()
#functions like append,remove, insert, reverse,sort can not be applied in tuple

#converting list to tuple and vice versa
my_new_tuple = (11,22,33)
new_list = list(my_new_tuple)
print(new_list)
str_list = ['one','two','three']
str_tuple = tuple(str_list)
print(str_tuple)