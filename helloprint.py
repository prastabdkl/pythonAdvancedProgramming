"""
print('Hello World')
print('I "love" Nepal')
print('I \n Love \n Nepal')
print(""Hello World I "love" Nepal I \n Love \n Nepal ")
print( "Monday's sales are", 123,
"and Tuesday's sales are", 456,
"and Wednesday's sales are", 789)

"""
print('One', end=' ')
print('Two', end=' ')
print('Three')

print('One', 'Two', 'Three', sep='~~~')

print('The number is', format(12345.6789, '12,.2f'))

print('Enter the amount of ' +
'sales for each day and ' +
'press Enter.')

""" #total = ( value1 + value2 +
            # value3 + value4 +
            # value5 + value6) """

brand= 'Apple'
exchangeRate=12.1231
message = 'The price of this %s laptop is %d USD and the exchange rate is %4.2f USD to 1 EUR' %(brand, 1299, exchangeRate)
print(message)
message = 'The price of this {0:s} laptop is {1:d} USD and the exchange rate is {2:4.2f} USD to 1 EUR'.format('Apple', 1299, 1.235235245)
print(message)

# Create two variables: top_speed and distance.
top_speed = 160
distance = 300

# Display the values referenced by the variables.
print('The top speed is')
print(top_speed)
print('The distance traveled is')
print(distance)

""" 
#input concatination
x=input('What is the value of x')
y=input('What is the value of y')

print(x+y)


#value addition
x=int(input('What is the value of x'))
y=int(input('What is the value of y'))

print(x+y)

#a program to input and show results
 # Get the user's name, age, and income.
name = input('What is your name? ')
age = int(input('What is your age? '))
income = float(input('What is your income? '))

 # Display the data.
print('Here is the data you entered:')
print('Name:', name)
print('Age:', age)
print('Income:', income)
 """