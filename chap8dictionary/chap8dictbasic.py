phonebook = {'Chris':'9800512346','Abdul':'566264135','Frank':'22563662'}
print(phonebook)

phonebook['Bobby']='985415445'
print(phonebook)

del phonebook['Abdul']
print(phonebook)

if 'chris' in phonebook:
    print(phonebook['chris'])

if 'ram' not in phonebook:
    print('Ram not found')

if 'Frank' in phonebook:
    del phonebook['Frank']

print(phonebook)

print('Length of phonebook is:',len(phonebook))