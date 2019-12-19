numbers = list(range(5))
print(numbers)
numbers = list(range(1, 10, 2))
print(numbers)
numbers = [1, 2, 3] * 3
print(numbers)
numbers = list(range(5))
print(numbers[:3])
print(numbers[2:])
print(numbers[:])

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[1:8:2])
print(numbers[-5:])

#searching using in and not in
prod_nums = ['V475', 'F987', 'Q143', 'R688']
search = input('Enter the element to search')
if search not in prod_nums:
    print(search, 'was not found in the list.')
else:
    print(search, 'was found in the list.')
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list3 = list1 + list2
print(list3)
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday',
'Thursday', 'Friday', 'Saturday']
mid_days = days[2:5]