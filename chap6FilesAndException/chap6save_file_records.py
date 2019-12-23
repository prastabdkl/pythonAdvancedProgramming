# This program gets employee data from the user and
# saves it as records in the employee.txt file.
# read the records and show until the end is reached
def write_records():
    # Get the number of employee records to create.
    num_emps = int(input('How many employee records ' +'do you want to create? '))
    # Open a file for writing.
    emp_file = open('employees.txt', 'w')
    # Get each employee's data and write it to the file.
    for count in range(1, num_emps + 1):
        # Get the data for an employee.
        try:
            print('Enter data for employee #', count, sep='')
            name = input('Name: ')
            id_num = int(input('ID number: '))
            dept = input('Department: ')
        except ValueError:
            print('invalid input: ValueError')

        # Write the data as a record to the file.
        emp_file.write(name + '\n')
        emp_file.write(str(id_num) + '\n')
        emp_file.write(dept + '\n')
        # Display a blank line.
        print()

    # Close the file.
    emp_file.close()
    print('Employee records written to employees.txt.')
    # Call the main function.

def read_records():
    try:
        infile = open('employes.txt','r')
        name = infile.readline()

        while name != '':
            id_num = infile.readline()
            dept = infile.readline()

            #print the data
            #name = name.rstrip()
            #id_num = id_num.rstrip()
            #dept =dept.rstrip()
            
            print('Name:',name,'id_num:',id_num,'dept:',dept,sep='')

            name = infile.readline()
        
        infile.close() 
    except Exception: 
        print('File not found')
        exit(0)

def search_records():
    found = False
    search = input('Enter the name you want to search?')
  
    emp_file = open('employees.txt','r')

    name = emp_file.readline() 

    while name != '':
        id_num = emp_file.readline()
        dept = emp_file.readline()

        name = name.rstrip()

        if name == search:
            print('Name:',name)
            print('id_num:',id_num,end='')
            print('Dept:',dept)
            found = True

        name = emp_file.readline()
    
    emp_file.close()

    if not found:
        print('The name',search,'was not found')
    
def main():
    write_records()
    read_records()
    search_records()
    
main()