import random
class Coin:
    #everything inside the class goes here
    #constructor
    def __init__(self):
        self.sideup = 'Heads'
    def toss(self):
        if random.randint(0,1) == 0: #random number selection between 0 and 1
            self.sideup = 'Heads'
        else:
            self.sideup = 'Tails'
    def get_sideup(self):
        return self.sideup

def main():
    my_coin = Coin() #creating object of Coin class
    #print(my_coin.sideup) #accessing initialized sideup variable
    my_coin.toss() #calling toss function
    print('We have',my_coin.get_sideup(),'in this toss') #printing toss variable after tossing

main()