#num= 64
flag=0
lower = int(input('Enter the lower limit'))
upper = int(input('Enter the upper limit'))

for num in range(lower,upper+1):
    flag = 0
    for count in range(2,num):
        if(num%count == 0):
            flag = 1
            break
    if flag == 0:
        print(num)

""" 
if(flag == 1):
    print(num,'is not prime')
else:
    print(num,'is prime') """