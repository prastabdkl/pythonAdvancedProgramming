rows,cols=2,3
""" 
rows = int(input('How many rows? '))
cols = int(input('How many columns? '))
 """
NUM_STEPS = 6

for r in range(rows):
    for c in range(cols):
        print('*', end='')
    print()

BASE_SIZE = 8

for r in range(BASE_SIZE):
    for c in range(r + 1):
        print('*', end='')
    print()    

for r in range(NUM_STEPS):
    for c in range(r):
        print(' ', end='')
    print('#')