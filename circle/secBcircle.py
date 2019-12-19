import circle
import random

AREA_CIRCLE_CHOICE = 1
CIRCUMFERENCE_CHOICE = 2
AREA_CYLINDER_CHOICE = 3
QUIT_CHOICE = 4

def display_menu():
    print('---------MENU----------')
    print('1) Area of Circle')
    print('2) Circumference of Circle')
    print('3) TSA of a cylinder')
    print('4) QUIT ')

def main():
    choice = 0
    while choice != QUIT_CHOICE:
        display_menu()
        choice = int(input('Enter your choice'))
        if choice == AREA_CIRCLE_CHOICE:
            radius = random.randint(10,50)
            print('The area of circle with radius',radius ,'is',circle.area(radius))
        elif choice == CIRCUMFERENCE_CHOICE:
            radius = random.randint(10,50)
            print('The circumference of circle with radius',radius ,'is',circle.circumference(radius))
        elif choice == AREA_CYLINDER_CHOICE:
            radius = random.randint(10,50)
            height = float(input('Enter the height'))
            print('The TSA of cyliner with radius',radius ,'and height',height,'is',
            2*circle.area(radius)+ height* circle.circumference(radius))
        elif choice == QUIT_CHOICE:
            print('The program will now exit')
        else:
            print('Invalid input')
main()