import tkinter as tk
from salary_tax_single import tax_calculation
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        # create a main window widget
        self.main_window = tk.Tk('Salary Tax Calulator')
        #self.main_window.geometry('1000x250'     
        self.create_GUI()
        #enter the tk mainloop
        self.main_window.mainloop()
        
    def create_GUI(self):
                #create 3 frames, 1st one for input, 2nd one for displaying results, 3rd one for buttons
        self.top_frame = tk.Frame(self.main_window,)
        self.mid_frame = tk.Frame(self.main_window)
        self.bottom_frame = tk.Frame(self.main_window)
        
        #for top frame
        self.label_monthly_salary = tk.Label(self.top_frame,\
            text='Enter your monthly salary',font=('Arial Bold',20))
        self.monthly_salary_entry = tk.Entry(self.top_frame,width = 10,font=('Arial Bold',15))    
        self.label_monthly_salary.pack(side='left')
        self.monthly_salary_entry.pack(side ='left')

        #for mid frame
        self.mid_frame1= tk.Frame(self.mid_frame)
        self.mid_frame2= tk.Frame(self.mid_frame)
        self.mid_frame3= tk.Frame(self.mid_frame)
        self.mid_frame4= tk.Frame(self.mid_frame)
        #values for each label
        self.value1 = tk.StringVar()
        self.value2 = tk.StringVar()
        self.value3 = tk.StringVar()
        self.value4 = tk.StringVar()

        self.label_value1 = tk.Label(self.mid_frame1,textvariable = self.value1,font=('Arial ',20))
        self.label_value2 = tk.Label(self.mid_frame2,textvariable = self.value2,font=('Arial ',20))
        self.label_value3 = tk.Label(self.mid_frame3,textvariable = self.value3,font=('Arial ',20))
        self.label_value4 = tk.Label(self.mid_frame4,textvariable = self.value4,font=('Arial ',20))

        self.label_monthly_salary_tax = tk.Label(self.mid_frame1,text = 'Monthly Tax:',font=('Arial ',20))
        self.label_monthly_salary_after_tax_deduction = tk.Label(self.mid_frame2,text = 'Monthly Salary Receiveable:',font=('Arial ',20))
        self.label_annual_salary_tax = tk.Label(self.mid_frame3,text = 'Annual tax:',font=('Arial ',20))
        self.label_annual_salary_after_tax_deduction = tk.Label(self.mid_frame4,text = 'Annual Salary receivable:',font=('Arial ',20))

        self.label_monthly_salary_tax.pack(side='left')
        self.label_value1.pack(side='left')
        self.label_monthly_salary_after_tax_deduction.pack(side='left')
        self.label_value2.pack(side='left')
        self.label_annual_salary_tax.pack(side="left")
        self.label_value3.pack(side="left")
        self.label_annual_salary_after_tax_deduction.pack(side="left")
        self.label_value4.pack(side="left")

        self.mid_frame1.pack(side='top')
        self.mid_frame2.pack(side='top')
        self.mid_frame3.pack(side='top')
        self.mid_frame4.pack(side='top')

        #for bottom frame
        self.calc_button = tk.Button(self.bottom_frame,text='CALCULATE',command= self.get_value,font=('Arial Bold',10))
        self.main_window.bind('<Return>',self.get_value)

        self.quit_button = tk.Button(self.bottom_frame,text= 'QUIT', command = self.main_window.destroy,font=('Arial Bold',10))
        self.calc_button.pack(side = 'left')
        self.quit_button.pack(side = 'left')

        #packing the frames
        self.top_frame.pack(side='top')
        self.mid_frame.pack(side='top')
        self.bottom_frame.pack(side='top')


    def get_value(self,Event=None):
        monthly_amount = float(self.monthly_salary_entry.get())
        tax_calculation(monthly_amount,self.value1,self.value2,self.value3,self.value4)

    

my_gui = MyGUI()