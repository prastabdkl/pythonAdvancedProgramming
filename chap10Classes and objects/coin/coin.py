import random
# The Coin class simulates a coin that can
# be flipped.
# Author: Prastab Dhakal
# Chapter: Classes and objects
class Coin:
    # The _ _init_ _ method initializes the
    # __sideup data attribute with 'Heads'.
    def __init__(self):
        self.__sideup = 'Heads'

    # The toss method generates a random number
    # in the range of 0 through 1. If the number
    # is 0, then __sideup is set to 'Heads'.
    # Otherwise, __sideup is set to 'Tails'.
    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'

    # The get___sideup method returns the value
    # referenced by __sideup.
    def get_sideup(self):
        return self.__sideup
