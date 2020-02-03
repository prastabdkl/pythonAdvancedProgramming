# a menu based program that will see a list of vegetables, add the list of vegetables
# change the price of it, delete the vegetable according to the input given by user.
# Author: Prastab Dhakal
# Chapter: Dictionary

vegetables = {"Tomato":'25',"potato":'40',"onion":'250',"Cabbage":'100'}

def see_list():
    for key, value in vegetables.items():
        print (key,': Rs',value)
        
def add_vegetables():
    key = input("Enter the name of vegetables: ")
    val = input ("Enter the price of vegetables:")
    vegetables[key]= val
def change_price():
    key = input("Enter the name of vegetable to Change: ")
    val = input ("Enter the price of ",key," :")
    vegetables[key] = val
def delete_vegetables():
    key= input("Enter the name of vegetable to delete: ")
    vegetables.pop(key)

choice = 0
while choice!=5:
    print("1.List of Vegetables \n2.Add Vegetables \n3. Change Price \n4.Delete Vegetables \n5. Exit")
    choice = int(input("Enter your choice: "))
    if(choice==1):
        see_list()
    elif(choice==2):
        add_vegetables()
    elif(choice==3):
        change_price()
    elif(choice==4):
        delete_vegetables()
    elif(choice==5):
        exit()