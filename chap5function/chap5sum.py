#a program to input two numbers and find the sum
# 
# Author: Prastab Dhakal
# Chapter: functions
def calculate_sum(num1,num2):
    return num1+num2

def main():
    num1 = int(input('Enter a number'))
    num2 = int(input('Enter a number'))
    total = calculate_sum(num1,num2)
    print('The sum is ', total)

main()