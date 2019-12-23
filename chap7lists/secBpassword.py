#WAP that accepts a password when it has
#   at least
        # 1 digit,
        # 1 uppercase
        # 1 lowercase
        # 1 special character

digit_found = False
upper_found = False
lower_found = False
special_found = False

password_accepted = False
password = input('Enter a password')
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

    if digit_found and upper_found and lower_found \
        and special_found and len(password)>=8:
        print('password is valid')
        password_accepted = True
    else:
        password = input('password is not valid,Enter again')
