# passwords for the campus computer system must meet the following requirements:
# • The password must be at least seven characters long.
# • It must contain at least one uppercase letter.
# • It must contain at least one lowercase letter.
# • It must contain at least one numeric digit.

password_message = """Enter a password:
    The password must be at least seven characters long.
    • It must contain at least one uppercase letter.
    • It must contain at least one lowercase letter.
    • It must contain at least one numeric digit. \n"""

password = input(password_message)
password_accepted = False
alphabets = digits = special = 0

while password_accepted == False:
    if len(password)<7 or password.isspace() or password == '' or password.isalpha() or password.isdigit() or password.isupper() or password.islower():
        password = input(password_message)
    else:
        for i in range(len(password)):
            if(password[i].isalpha()):
                alphabets = alphabets + 1
            elif(password[i].isdigit()):
                digits = digits + 1
            else:
                special = special + 1
        if special == 0:
            password = input(password_message)
        else:
            password_accepted = True

print(password)
# if len(password)
