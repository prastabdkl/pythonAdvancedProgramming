#password = input('Enter password')
#password = '11111111'
#password = 'aaaaaaaa'
password = 'AAAAAAAA'
#password = '        '
#password = 'aaaAAA1111'
#password = 'aaaAAA111@'

print(password)
#returns true if string contains only special characters and is at least one character in length
def is_special(password):
    special = 0
    for i in range(len(password)):
        if not(password[i].isalpha() or password[i].isdigit()):    
            special += 1

    if special == len(password):
        return True
    elif special == 0:
        return True
    else:
        return False


password_valid = False
while password_valid == False:
    print('all or one Digits',password.isdigit())
    print('all or one alpha',password.isalpha())
    print('all or one space',password.isspace())
    print('all or one upper',password.isupper())
    print('all or one special',is_special(password))

    if password.isdigit() or password.isalpha() \
        or password.isspace() or password.isupper() \
        or password ==  '' or len(password)<8 \
        or is_special(password):
        print('password is not valid')
        password = input('Enter password')
    else:
        print('valid password')
        password_valid = True

print(is_special(password))

