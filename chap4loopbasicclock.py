import time
for hours in range(24):
    for minutes in range(60):
        for seconds in range(60):
            print('%02d:%02d:%02d'%(hours,minutes,seconds))
            #print(hours, ':', minutes, ':', seconds)
            time.sleep(1)

#WAP to show prime numbers 
#of a given range by user using loop