def main():

    #Input the names of three friends
    name1 = input('Friend 1:')
    name2 = input('Friend 2:')
    name3 = input('Friend 3:')

    myfile = open('my_friends.txt','w')

    myfile.write(name1 + '\n')
    myfile.write(name2 + '\n')
    myfile.write(name3)

    myfile.close()

    readfile = open('my_friends.txt','r')
    file_contents = readfile.read()
    readfile.close()
    print(file_contents)    
main()