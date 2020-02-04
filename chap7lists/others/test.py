def is_not_special(password):
    for i in range(len(password)):
        if password[i].isalpha() or password[i].isdigit():
            print('IF')    
            continue
        else:
            print('ELSE')
            return False
    return True

status = is_not_special('ADCaad32')
print(status)