# Encrypt the 5 digit password using a dictionary
# 	1: '@', 2: '$', 3:'*', ....... 9:'&',0:'^'
# 	show the encrpted password
# 	ask the user if he wants to decrypt it
# 	show the decrpted password

#Author: Anil Khatiwada
def get_key(encrypted): 
    decrypted =''
    for x in encrypted:
        for key, value in symbol_assign.items():
            if x == value: 
                decrypted = decrypted + key 
    return decrypted

symbol_assign = {'1':'!','2':'@','3':'#','4':'$','5':'%','6':'^','7':'&','8':'*','9':'(','0':')'}
pass_word = input("Enter your password: ")
while len(pass_word)!=5:
    pass_word = input("Please use 5 digit number, Enter your password: ")
encrypted =''
for x in range (0,5):
    encrypted= encrypted + symbol_assign[pass_word[x]]

print ("Your Encrypted password is: ",encrypted)
choice = input("Do you wanna decrypt it again ? y/n?  : ")
if(choice=='y' or choice=='Y'):
    print ("Your Decrypted password is ", get_key(encrypted))
elif(choice =='n' or choice=='N'):
    exit()
else:
    print("Input is invalid")