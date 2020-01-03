import circle
import random

def main():
    radius = random.randrange(1,10)
    #radius = float(input('Enter the radius of the cylinder'))
    height = float(input('Enter the height of cylinder'))

    TSA = 2 * circle.area(radius) + height* circle.circumference(radius)
    print(TSA)
main()