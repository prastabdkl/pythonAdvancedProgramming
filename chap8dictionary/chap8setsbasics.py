# Basics of Sets
# Author: Prastab Dhakal
# Chapter: Dictionary and sets
myset = set('abc')
print(myset)
myset = set('aaabc')#does not take duplicates
print(myset)

myset = set('one two three') #takes single element
print(myset)
myset = set(['one', 'two', 'three'])#keeps as an element
print(myset)

myset1 = set('[12,33,13]') #removes duplicates
print('len of', myset1, 'is:',len(myset1))

myset2 = set([12,33,13])
print('len of', myset2, 'is:',len(myset2))
#adding elements in set
myset = set() 
myset.add(10) 
myset.add(20) 
myset.add(30) 
print(myset)
myset.add(3) 
print(myset)

myset = set([1, 2, 3])
myset.update([4, 5, 6])
print(myset) 

set1 = set([10, 20, 30])
set2 = set([40, 50, 60])

set1.update(set2)
print(set1) 
#set1.remove(5)

print("remove:",set1) #gives keyerror
set1.discard(5)
print("discard",set1)

myset = set(['a', 'b', 'c']) 

for val in myset:
    print(val)

# search_key = input('Enter what you want to search:')
# if search_key in myset:
#     print(search_key, 'is in the set')
# else:
#     print(search_key,'not found')

set1 = set([1,2,3,4])
set2 = set([3,4,5,6])
#union
set3 = set1.union(set2)
print('Set1:',set1,'\nSet2:',set2,'\nUnified Set3:',set3)
set3 = set1 | set2
print('Set1:',set1,'\nSet2:',set2,'\nUnified Set3:',set3)
#intersection
set3 = set1.intersection(set2)
print('Set1:',set1,'\nSet2:',set2,'\nIntersection Set3:',set3)
set3 = set1 & set2
print('Set1:',set1,'\nSet2:',set2,'\nIntersection Set3:',set3)
#difference
set3 = set1.difference(set2)
print('Set1:',set1,'\nSet2:',set2,'\nDifference Set3:',set3)
set3 = set1 - set2
print('Set1:',set1,'\nSet2:',set2,'\nDifference Set3:',set3)
#symmetric_difference
set3 = set1.symmetric_difference(set2)
print('Set1:',set1,'\nSet2:',set2,'\n symmetric_difference Set3:',set3)
set3 = set1 ^ set2
print('Set1:',set1,'\nSet2:',set2,'\n symmetric_difference Set3:',set3)

set1 = set([1, 2, 3, 4]) 
set2 = set([2, 3]) 
print(set2.issubset(set1)) 
print(set2 <= set1) 

print(set1.issuperset(set2)) 
print(set1 >= set2) 
