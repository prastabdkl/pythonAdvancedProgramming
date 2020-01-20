dict1  = {'ram':1234, 'shyam':5678, 'hari':45568}

dict2 = {}
# no_of_terms = int(input('Enter the number of terms'))
# for i in range(no_of_terms):
#     key = input('Enter the key')
#     value = input('Enter the value')
#     dict2[key] = value # append a new value to the dictionary
print(dict2)

new_data = dict([('ram',1234),('shyam',5678),('harry',54658)])
print(new_data)

#new_dict1 = {x:y for x in (2,4,6)}
#print(new_dict1)
#X=(1,2,3) Y=(1,2,3)
#cartisian product in dictionary form: X x Y
#{1:2,1:3,2:1 ... ,3:2}
cartisian = {}
list1= []
for x in [1,2,3]:
    for y in [1,2,3]:
        if x != y:
            cartisian[x] = y
            list1.append((x, y))

print("cartisian:",cartisian,"list:",list1)

dict1  = {'ram':1234, 'shyam':5678, 'hari':45568}
for key,value in dict1.items():
    print(key,value)

for key in dict1.keys():
    print(key)

for val in dict1.values():
    print(val)

for index,key in enumerate(dict1): #returns index and key
    print(index,key)

value = dict1.get('Ram','Such Key doesnot exist')
print(value)

value = dict1.pop('ram','no such key found') #remove item ac/t to key
print(dict1)
key,value = dict1.popitem() #randomly delete an item
print(dict1)
dict1.clear()
print(dict1)