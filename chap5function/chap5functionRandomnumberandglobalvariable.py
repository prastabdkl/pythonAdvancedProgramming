# A program to print random numbers within a range
# Author: Prastab Dhakal
# Chapter: functions
import random
#  Create a global variable.
number = 0

def main():
    global number
    number = int(input('Enter a % number: '))
    
    for count in range(5):
        number2 = random.randint(1,100)
        print('Random number is:',number2)
    
    show_number()

def show_number():
    print('The number you entered is', number)

# Call the main function.
main()