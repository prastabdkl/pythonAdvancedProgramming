myset = set('abc')
print(myset)
myset = set('aabbc')
print(myset)
myset = set('one two three')
print(myset)
myset = set(['one','two','three'])
print(myset)
myset = set([11,22,33])
print(myset)
myset = set('[11,22,33]')
print(myset)

myset = set()
myset.add(10)
myset.add(20)
print(myset)
myset.add(30)
print(myset)

myset1 = set([1,2,3])
myset.update(myset1)
print(myset,len(myset))

myset.remove(3)
print(myset)
myset.discard(5)
print(myset)

for value in myset:
    print(value)

# search_key = int(input('Enter a search key'))
# if search_key in myset:
#     print(search_key,'found')
# else:
#     print(search_key,'not found')

#union
set1 = set([1,2,3,4])
set2 = set([3,4,5,6])

set3 = set1.union(set2)
print('Set1:',set1,'set2:',set2,'unified set',set3)
print('Set1:',set1,'set2:',set2,'unified set',set1 | set2)

set3 = set1.intersection(set2)
print('Set1:',set1,'set2:',set2,'intersection set',set3)
print('Set1:',set1,'set2:',set2,'intersection set',set1 & set2)

set3 = set1.difference(set2)
print('Set1:',set1,'set2:',set2,'difference set',set3)
print('Set1:',set1,'set2:',set2,'difference set',set1 - set2)

set3 = set1.symmetric_difference(set2)
print('Set1:',set1,'set2:',set2,'symmetric_difference set',set3)
print('Set1:',set1,'set2:',set2,'symmetric_difference set',set1 ^ set2)

set1 = set([1,2,3,4])
set2 = set([3,4])

print(set2.issubset(set1),'or',set2 <= set1)
print(set2.issuperset(set1),'or',set2 >= set1)