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

"""
1 2 3 4 5
for i=1;i<=5;i++
    print(i)

for i in [1,2,3,4,5]:
    print(i)
for name in ['ram','am','jam']:
    print(name)
 #range starts form 0 and ends to -1 value   
for num in range(100):
    print(num)
#first argument is start point and second end point
for num in range(1,100):
    print(num)
for num in range(5):
    print('Hello')

#1 and 10 start and resp and 2 is step
for num in range(1,10,2):
    print(num)
WAFL to find square of even numbers form
10 20 included

WAP to show a digital clock starting form
00:00:00
and ending at
23:59:59


"""