#a program to input a number and find the square of that number
# 
# Author: Prastab Dhakal
# Chapter: functions
def main():
    number= int(input('Enter a number'))
    calculate_square(number)

def calculate_square(number):
    square =number*number
    print('The square of ',number,'is',square)
    print('The square of ',number+1,'is',pow(number+1,2))

main()

