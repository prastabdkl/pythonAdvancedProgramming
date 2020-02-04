# Write a program to generate employee records:
def write_function():
    # Your program should ask the number of employees
    # Enter the following details of each employee:
    #     name,ID(int),dept
    # Check for Value errors and handle the error accordingly
    num_emps =int(input('Enter the number of employees'))
    emp_file = open('employees.txt','w')

    for count in range(num_emps):
        print('Enter the data for Employee #',count+1)
        name = input('Name:')
        flag = 0
        while  flag == 0:
            try:
                ID = int(input('ID number:'))
                flag = 1
            except Exception as E:
                print('\t ID must be integer,enter valid ID',E)
        dept = input('Department:')

        emp_file.write(name+'\n')
        emp_file.write(str(ID)+'\n')
        emp_file.write(dept+'\n')
        print()

def read_function():
    # The function should show the records entered.
    # Check for filenotfound 
    try:
        emp_file = open('employees.txt','r')
    except Exception as E:
        print('File not found',E)
    
    name = emp_file.readline()
    while name != '':
        id_num = emp_file.readline()
        dept = emp_file.readline()
        
        name = name.rstrip('\n')
        id_num =id_num.rstrip('\n')
        dept = dept.rstrip('\n')

        print('Name:',name)
        print('ID Number:',id_num)
        print('Department:',dept)
        print()

        name = emp_file.readline()


def search_according_to_name():
    # This function will show the employee details according to search key
    try:
        emp_file = open('employees.txt','r')
    except Exception as E:
        print('File not found',E)
    search_key = input('Enter the employee name you want to search')
    
    name = emp_file.readline()
    found = False
    while name != '':
        id_num = emp_file.readline()
        dept = emp_file.readline()
        
        name = name.rstrip('\n')
        id_num =id_num.rstrip('\n')
        dept = dept.rstrip('\n')
        if name == search_key:
            print('Name:',name)
            print('ID Number:',id_num)
            print('Department:',dept)
            found = True
        name = emp_file.readline()
    if not found:
        print('The name',search_key,'is not in the record')

def main():
    # call all the functions here
    write_function()
    read_function()
    search_according_to_name()
main()