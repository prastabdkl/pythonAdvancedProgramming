correct_length = False
has_uppercase = False
has_lowercase = False
has_digit = False
# Begin the validation. Start by testing the
# password's length.
password = input('Enter a valid password')
if len(password) >= 7:
    correct_length = True
# Test each character and set the
# appropriate flag when a required
# character is found.
for ch in password:
    if ch.isupper():
        has_uppercase = True
    if ch.islower():
        has_lowercase = True
    if ch.isdigit():
        has_digit = True
# Determine whether all of the requirements
# are met. If they are, set is_valid to true.
# Otherwise, set is_valid to false.
if correct_length and has_uppercase and \
    has_lowercase and has_digit:
    is_valid = True
    print('password is valid')
else:
    is_valid = False
    print('password not valid')
# Return the is_valid variable.
