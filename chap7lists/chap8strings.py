string ='The beauty of mountain is only seen when you actually visit the mountain'
count_a = count_t = 0
for char in string:
    print(char)
    if char == 'a' or char == 'A':
        count_a += 1
    if char == 't' or char == 'T':
        count_t += 1

print(string)
print('The number of a',count_a)
print('The number of b',count_t)
count_a =count_t = 0
for count in range(len(string)):
    print(string[count])
    if string[count] == 'a' or string[count] == 'A':
        count_a += 1
    if string[count] == 't' or string[count] == 'T':
        count_t += 1
print(string)
print('The number of a',count_a)
print('The number of b',count_t)