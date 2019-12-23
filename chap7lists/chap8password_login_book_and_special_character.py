digit_found = False
upper_found = False
lower_found = False
special_found = False

#password = input('Enter password')
#password = '11111111'
#password = 'aaaaaaaa'
#password = 'AAAAAAAA'
#password = '        '
#password = 'aaaAAA1111'
password = '1111111@@@@'
print(password)
password_valid = False
while password_valid == False:
    for i in range(len(password)):
        if password[i].isdigit():
            digit_found = True
        if password[i].isupper():
            upper_found = True
        if password[i].islower():
            lower_found = True 
        if not(password[i].isdigit()) and not(password[i].isupper()) and not(password.islower()):
            special_found = True
    if digit_found and upper_found and lower_found and not(password.isspace()) and password != '' and special_found:
        print('valid password')
        password_valid = True
    else: 
        print('Invalid password')
        password = input('Enter a valid password')

    # print('Digit is found',digit_found)
    # print('Upper case found',upper_found)
    # print('Lower case found',lower_found)
    # print('special case found',special_found)

#returns true if string contains only special characters and is at least one character in length
# def is_special(password):
#     special = 0
#     for i in range(len(password)):
#         if not(password[i].isalpha() or password[i].isdigit()):    
#             special += 1

#     if special == len(password):
#         return True
#     elif special == 0:
#         return True
#     else:
#         return False