# This program gets an item's original price and
# calculates its sale price, with a 20% discount and 13% VAT.
# Author: Prastab Dhakal
# operators and formatting

# Get the item's original price.
original_price = float(input("Enter the item's original price: "))

# Calculate the amount after 10% the discount.
discount = original_price * 0.1

# Calculate the sale price.
sale_price_before_VAT = original_price - discount

sale_price_after_VAT= 1.13*sale_price_before_VAT

# Display the sale price.
print('The sale price is','%.2f' %sale_price_after_VAT)

#operators + - * / % //(integer division) **(exponent)

# x,y=5,5
# value=x**2+3*x*y+y**2
# print(value)

# marked_price = float(input('Enter the marked price: '))

# price_after_discount_VAT = marked_price*0.9*1.13
# print('%.2f'%price_after_discount_VAT)