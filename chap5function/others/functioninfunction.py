# have local variables with the same name.
# This program demonstrates two functions that
def main():
    # Call the texas function.
    texas()
    # Call the california function.
    california()
    # Definition of the texas function. It creates
    # a local variable named birds.

def texas():
    birds = 5000
    print('Texas has', birds, 'birds.')
    # Definition of the california function. It also
    # creates a local variable named birds.

def california():
    birds = 8000
    print('California has', birds, 'birds.')
# Call the main function.
main()