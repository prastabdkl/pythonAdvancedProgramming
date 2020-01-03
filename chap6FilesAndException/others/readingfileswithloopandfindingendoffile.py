# This program reads all of the values in
# the sales.txt file.
def write_into_file():
    # Get the number of days.
    num_days = int(input('For how many days do ' +
    'you have sales? '))
    # Open a new file named sales.txt.
    sales_file = open('sales.txt', 'w')
    # Get the amount of sales for each day and write
    # it to the file.
    for count in range(1, num_days + 1):
        # Get the sales for a day.
        sales = float(input('Enter the sales for day #' +
        str(count) + ': '))
        # Write the sales amount to the file.
        sales_file.write(str(sales) + '\n')
    # Close the file.
    sales_file.close()

def main():
    # Open the sales.txt file for reading.
    write_into_file()
    sales_file = open('sales.txt', 'r')
    # Read the first line from the file, but
    # don't convert to a number yet. We still
    # need to test for an empty string.
    line = sales_file.readline()
    # As long as an empty string is not returned
    # from readline, continue processing.
    while line != '':
        # Convert line to a float.
        amount = float(line)
        # Format and display the amount.
        print(format(amount, '.2f'))
        # Read the next line.
        line = sales_file.readline()
    # Close the file.
    sales_file.close()
# Call the main function.
main()