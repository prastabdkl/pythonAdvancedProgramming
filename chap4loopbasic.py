print('I will display the numbers 1 through 5.')
for num in [1, 2, 3, 4, 5]:
    print(num)

for num in range(5):
    print(num)
#this is same as
for num in [0, 1, 2, 3, 4]:
    print(num)

for x in range(5):
    print('Hello world')

for num in range(1, 5): #starts from 1 and ends at 4 so prints 1,2,3,4
    print(num)

for num in range(1, 10, 2): #1 is the start value, 9 is the end value, 2 is the step: output:1,3,5,7,9
    print(num)

print('Number\tSquare')
print('--------------')

# Print the numbers 1 through 10
# and their squares.
for number in range(1, 11):
    square = number**2
    print(number, '\t', square)