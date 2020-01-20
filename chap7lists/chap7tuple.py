#basics of tuple
# Author: Prastab Dhakal
# Chapter: Lists and tuples

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
#append, remove, insert, reverse, and sort. do not work in tuple
my_tuple = (1,) # Creates a tuple with one element.
value = (1) # Creates an integer.

#converting between lists and tuple
number_tuple = (1, 2, 3)
number_list = list(number_tuple) 
print(number_list) 
#[1,2,3]
str_list = ['one', 'two', 'three'] 
str_tuple = tuple(str_list) 
print(str_tuple)
#('one', 'two', 'three')
