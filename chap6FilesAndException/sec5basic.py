#write
outfile = open('text.txt','w')
outfile.write(str(12)+'\n')
outfile.write(str(15)+'\n')
outfile.write(str(20))
outfile.close()
#read
infile = open('text.txt','r')
#operations
#file_contents = infile.read()
#print(file_contents)
line1 = infile.readline()
line1 = line1.rstrip('\n')
print(line1)
line2 = infile.readline()
print(line2)
infile.close()
# WAP to INPUT 5 sales data in a file(either int or float) use functions
#     READ the contents of the file 
#     push to contents to a list
#     show a pie chart with title, label and color
# Implement functions