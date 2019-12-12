# This program writes three lines of data
# to a file.
def main():
    # Open a file named philosophers.txt.
    infile = open(r'C:\Users\Sunway\Documents\P\pythonAdvancedProgramming\circle\hello.txt', 'r')

    # Close the file.
    file_contents = infile.read()
    infile.close()

    print(file_contents)

# Call the main function.
main()