tax_first=0.01
tax_second=0.1
tax_third=0.2
tax_fourth=0.3
tax_remain=0.36

def tax_calulation(amount,first,second,third,fourth):
  
    if(amount<=first):
        tax=tax_first*amount
    elif(amount<=first+second):
        tax=first*tax_first+(amount-first)*tax_second
    elif(amount<=first+second+third):
        tax=first*tax_first+second*tax_second+(amount-(first+second))*tax_third
    elif(amount<=first+second+third+fourth):
        tax=first*tax_first+second*tax_second+third*tax_third+(amount-(first+second+third))*tax_fourth
    else:
        tax=first*tax_first+second*tax_second+third*tax_third+fourth*tax_fourth+(amount-(first+second+third+fourth))*tax_remain

    return tax

def main():
    flag=0
    monthly_salary=float(input("Enter your monthly salary :"))

    while(monthly_salary<0):
        print('Invalid Salary!!!')
        monthly_salary=float(input("Enter your monthly salary :"))

    annual_salary=12*monthly_salary

    status=input("If you are single type 's' and if you are married type 'm' :")
    if(status=='s'or status=='S'):
        first=400000
        second=100000
        third=200000
        fourth=1300000
        tax=tax_calulation(annual_salary,first,second,third,fourth)
        flag=1
    elif(status=='m'or status=='M'):
        first=450000
        second=100000
        third=200000
        fourth=1250000
        tax=tax_calulation(annual_salary,first,second,third,fourth)
        flag=1 
    else:
        print("Invalid choice of status!!!")

    if(flag==1):
        print("Your annual salary is ",annual_salary,"so you have to pay ",tax," tax to the goverment .")



main()