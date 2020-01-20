# All the basics and functions of dictionary
# Author: Prastab Dhakal
# Chapter: Dictionary

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
#phonebook.clear()
#print(phonebook)


#dictionary.get(key, default)
value = phonebook.get('Andy', 'Entry not found')
print(value)
phonebook = {'Chris':'555−1111', 'Katie':'555−2222', 'Joanne':'555−3333'}
for key, value in phonebook.items():
    print(key, value)

for key in phonebook.keys():
    print(key)

for val in phonebook.values():
    print(val)

#dictionary.pop(key, default)
phone_num = phonebook.pop('Chris', 'Entry not found')
print(phone_num)

phone_num = phonebook.pop('Andy', 'Element not found')
print(phone_num)

#k,v = dictionary.popitem()
key, value = phonebook.popitem()
print(key,':',value)

dict1 = {}
# for i in range(3):
#     key = input('Enter key')
#     value = input('Enter value')
#     dict1[key] = value

print(dict1)

dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])

{x: x**2 for x in (2, 4, 6)}

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

squares = [x**2 for x in range(10)]
#squares = list(map(lambda x: x**2, range(10)))

[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))
print("combs:",combs)
"""
dict1 = {'ram':1234,'shyam':4567,'hari':'Harry'}
print(dict1)
print(dict1['ram'])

dict2 = {}
#no_of_terms =int(input('How many terms'))
# for i  in range(no_of_terms):
#     key = input('Enter a key')
#     value = input('Enter a value')
#     dict2[key] = value
print(dict2)
new_dict = dict([('ram',4139),('shyam',4568)])
print(new_dict)
new_dict1 = {x: x**2 for x in (2,4,6)}
print(new_dict1)
for k,v in new_dict1.items(): #to get key and value
    print(k,v)
for i,v in enumerate(new_dict1):#to get index and value
    print(i,v)
for key in new_dict1.keys():#to get keys
    print(key)
for value in new_dict1.values():# to get values
    print(value)
value = new_dict1.get(3,'Value not found') #dictionay.get(key,default)
print(value)
#dictionary.pop(key,default)
print(new_dict1)
value = new_dict1.pop(2,'Entry not found')#pop by key
print(new_dict1)
key, value = new_dict1.popitem()#pop randomly
print(key,value)
new_dict1.clear()#claer the dictiionary
print(new_dict1)






"""
