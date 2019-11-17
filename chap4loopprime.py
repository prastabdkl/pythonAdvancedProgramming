num= 64
flag=0

for count in range(2,num):
    if(num%count == 0):
        flag = 1
        break

if(flag == 1):
    print(num,'is not prime')
else:
    print(num,'is prime')