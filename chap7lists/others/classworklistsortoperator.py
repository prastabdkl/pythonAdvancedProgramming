from operator import itemgetter
# master=[]
# for i in range(3):
#     st = {}
#     name = input("Name>")
#     age = int(input("Age>"))
#     pincode=input("pincode>")
#     st['name']=name
#     st['age']=age
#     st['pincode']=pincode
#     master.append(st)

# print (master)

# st['name']="ram"

student_file =[['ram',2,9850],['shyam',6,1234],['Hari',1,2356]]
# student_file =[('ram',2,9850),('shyam',6,1234),('Hari',1,2356)]

a =sorted(student_file, key=itemgetter(1))
print(a)
