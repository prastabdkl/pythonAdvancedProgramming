# a program that writes integers in a file retrives them and converts it into a pie chart
# Author: Prastab Dhakal
# Chapter: files, list and matplotlib

# outfile = open('text.txt','w')
# outfile.write(str(12)+'\n')
# outfile.write(str(15)+'\n')
# outfile.write(str(20))
# outfile.close()
# #read
# infile = open('text.txt','r')
# #operations
# #file_contents = infile.read()
# #print(file_contents)
# line1 = infile.readline()
# line1 = line1.rstrip('\n')
# print(line1)
# line2 = infile.readline()
# print(line2)
# infile.close()
# WAP to INPUT 5 sales data in a file(either int or float) use functions
#     READ the contents of the file 
#     push to contents to a list
#     show a pie chart with title, label and color
# Implement functions
""" WAP to input 5 sales data in a file(either int or float) use functions read the contents of the file,
 push to contents to a list ,show a pie chart with title , label and color and implement function """

import matplotlib.pyplot as plt
data=open('data.txt','w')
data.write(str(30)+'\n')
data.write(str(10)+'\n')
data.write(str(20)+'\n')
data.write(str(70)+'\n')
data.close()

read=open("data.txt",'r')
data1=read.readline()
data1=data1.rstrip("\n")
data2=read.readline()
data2=data2.rstrip("\n")
data3=read.readline()
data3=data3.rstrip("\n")
data4=read.readline()
data4=data4.rstrip("\n")
list=[data1,data2,data3,data4]

labels = list
sizes = [215, 130, 245, 210]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # explode 1st slice

# Plot
# plt.pie(sizes, explode=explode, labels=labels, colors=colors,
# autopct='%1.1f%%', shadow=True, startangle=140) #autopct text inside the pie chart
plt.pie(labels, explode=explode,labels = labels,colors =colors,startangle=0,autopct='%1.1f%%')
plt.axis('equal')
plt.title("Our classwork")
plt.show()
read.close()