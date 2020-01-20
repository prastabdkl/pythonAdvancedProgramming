# a program to learn about readline,rstrip and exception handling when file not found
# This program reads the contents of the
# hello.txt file one line at a time.
# Author: Prastab Dhakal
# Chapter: Files and Exception


def main():
    #open a file named hello.txt in read mode
    try:
        infile = open('hello.txt','r')
    except FileNotFoundError: # as E:
        print('File not found')


    #read the files content and save it
    # to a variables

    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()

    line1 = line1.rstrip('\n')
    line2 = line2.rstrip('\n')

    #close the file
    infile.close()
    print(line1,line2,line3)

    print(line1)
    print(line2)
    print(line3)
main()