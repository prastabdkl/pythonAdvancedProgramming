# Author: Prastab Dhakal
# Chapter: Classes and objects

import coin
# The main function.
def main():
    # Create an object from the Coin class.
    my_coin = coin.Coin()
    # Display the side of the coin that is facing up.
    print('This side is up:', my_coin.get_sideup())
    # Toss the coin.
    # Toss the coin.
    print('I am going to toss the coin ten times:')
    for count in range(10):
        my_coin.toss()
        print(my_coin.get_sideup())

# Call the main function.
main()