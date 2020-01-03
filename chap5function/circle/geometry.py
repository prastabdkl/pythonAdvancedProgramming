# This program allows the user to choose various
# geometry calculations from a menu. This program
# imports the circle and rectangle modules.
import circle
# Constants for the menu choices
AREA_CIRCLE_CHOICE = 1
CIRCUMFERENCE_CHOICE = 2
AREA_CYLINDER_CHOICE = 3
QUIT_CHOICE = 4
# The main function.
def main():
    # The choice variable controls the loop
    # and holds the user's menu choice.
    choice = 0
    while choice != QUIT_CHOICE:
        # display the menu.
        display_menu()
        # Get the user's choice.
        choice = int(input('Enter your choice: '))
        # Perform the selected action.
        if choice == AREA_CIRCLE_CHOICE:
            radius = float(input("Enter the circle's radius: "))
            print('The area is', circle.area(radius))
        elif choice == CIRCUMFERENCE_CHOICE:
            radius = float(input("Enter the circle's radius: "))
            print('The circumference is',circle.circumference(radius))
        elif choice == AREA_CYLINDER_CHOICE:
            radius = float(input("Enter the circle's width: "))
            height = float(input('Enter the height of cylinder'))
            area = 2 * circle.area(radius)+ circle.circumference(radius)*height
            print('The total area of cylinder is', area)
        elif choice == QUIT_CHOICE:
            print('Exiting the program. . .')
        else:
            print('Error: invalid selection.')
# The display_menu function displays a menu.
def display_menu():
    print('MENU')
    print('1) Area of a circle')
    print('2) Circumference of a circle')
    print('3) Total Area of a closed Cylinder')
    print('4) Quit')
# Call the main function.
main()