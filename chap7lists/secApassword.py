digit_found = False
upper_found = False
lower_found = False
special_found = False

password = input('Enter a valid password')
password_accepted = False
while password_accepted == False:
    for char in password:
        if char.isdigit():
            digit_found = True
        if char.isupper():
            upper_found = True
        if char.islower():
            lower_found = True
        if not(char.isdigit()) and not(char.isalpha()):
            special_found = True

    # print('digit found',digit_found)
    # print('upper_found',upper_found)
    # print('lower_found',lower_found)

    if digit_found and upper_found and lower_found and special_found \
        and password != '' and len(password) >= 8 \
        and not(password.isspace()) :
        print('Valid password')
        password_accepted = True
    else:
        password =input('Invalid password! Enter a valid password')
