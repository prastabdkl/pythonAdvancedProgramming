import tkinter
import tkinter.messagebox

def tax_calculation(monthly_amount,value1,value2,value3,value4):
    tax_first=0.01
    tax_second=0.1
    tax_third=0.2
    tax_fourth=0.3
    tax_remain=0.36

    first=400000
    second=100000
    third=200000
    fourth=1300000

    # monthly_amount = float(self.monthly_salary_entry.get())
    amount = monthly_amount*12
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

    value1.set(tax/12)
    value2.set(monthly_amount-tax/12)
    value3.set(tax)
    value4.set((monthly_amount-tax/12)*12)
    # tkinter.messagebox.showinfo('Response',str(tax)+'Thanks for clicking the button.')