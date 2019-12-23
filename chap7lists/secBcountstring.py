#WAP to count the number of 'a' and 't' in the above string.
string = 'The beauty of mountain is seen actually when you visit the mountain.'

count_a = count_t = 0

for char in string:
    if char == 'a' or char == 'A':
        count_a += 1
    if char == 't' or char ==  'T':
        count_t += 1

print(string)
print('Count of a',count_a)
print('count of t',count_t)

count_a = count_t =0
for i in range(len(string)):
    if string[i] == 'a' or string[i] == 'A':
        count_a += 1
    if string[i] == 't' or string[i] =='T':
        count_t += 1

print(string)
print('Count of a',count_a)
print('count of t',count_t)
