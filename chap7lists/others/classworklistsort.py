from operator import itemgetter
student_file =[['ram',2,9850],['shyam',6,1234],['Hari',1,2356]]

print(student_file)
a=sorted(student_file, key=lambda student_file: student_file[1]) 
print(a)

b= sorted(student_file, key=itemgetter(1))
print(b)