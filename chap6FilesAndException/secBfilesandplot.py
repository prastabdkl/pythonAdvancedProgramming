########writing into a file
outfile = open('newfile.txt','w')

outfile.write('ram \n')
outfile.write('shyam \n')
outfile.write(str(15))

outfile.close()

########reading the contents of file
infile = open('newfile.txt','r')

#file_contents = infile.read()
#print(file_contents)

line1 = infile.readline()
line1 = line1.rstrip('\n')

print(line1)

line2 = infile.readline()
line2 = line2.rstrip('\n')

print(line2)

infile.close()