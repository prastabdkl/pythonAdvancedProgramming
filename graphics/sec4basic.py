import tkinter

class MyGUI:
    def __init__(self):
        # create a main window widget
        self.main_window = tkinter.Tk()
        #self.main_window.geometry('1000x250')

        #create 3 frames, 1st one for input, 2nd one for displaying results, 3rd one for buttons
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        
        #for top frame
        self.label_monthly_salary = tkinter.Label(self.top_frame,\
            text='Enter your monthly salary')
        self.monthly_entry = tkinter.Entry(self.top_frame,width = 10)    
        self.label_monthly_salary.pack(side='left')
        self.monthly_entry.pack(side ='left')

        #packing the frames
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()     

        #enter the tkinter mainloop
        self.main_window.mainloop()

my_gui = MyGUI()