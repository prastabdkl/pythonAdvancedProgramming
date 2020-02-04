# This program creates labels in two different frames.
import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        # Create the main window widget.
        self.main_window = tkinter.Tk()
        self.main_window.geometry('1250x250')
        # Create two frames, one for the top of the
        # window, and one for the bottom.
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        # Create three Label widgets for the
        # top frame.
        self.label1 = tkinter.Label(self.top_frame,text = 'First Line',font=('Arial Bold',50))
        self.label2 = tkinter.Label(self.top_frame,text = 'Second Line')
        self.label3 = tkinter.Label(self.top_frame,text = 'Third Line')
        # Pack the labels that are in the top frame.
        # Use the side='top' argument to stack them
        # one on top of the other.
        self.label1.pack(side='top')
        self.label2.pack(side='top')
        self.label3.pack(side='top')
        self.top_frame.pack()
        # Create three Label widgets for the
        # bottom frame.
        self.my_button = tkinter.Button(self.main_window,text='Click Me!',command=self.do_something)
        self.my_button.pack()

        self.label4 = tkinter.Label(self.bottom_frame,text='First')
        self.label5 = tkinter.Label(self.bottom_frame,text='Second')
        self.label6 = tkinter.Label(self.bottom_frame,text='Third')
        # Pack the labels that are in the bottom frame.
        # Use the side='left' argument to arrange them
        # horizontally from the left of the frame.
        self.label4.pack(side='left')
        self.label5.pack(side='left')
        self.label6.pack(side='left')
        # Yes, we have to pack the frames too!
        self.bottom_frame.pack()

        self.quit_button = tkinter.Button(self.main_window,text='Quit',command=self.main_window.destroy)
        self.quit_button.pack()
        # Enter the tkinter main loop.
        tkinter.mainloop()

    def do_something(self):
        #display an info dialog box.
        #title and message
        tkinter.messagebox.showinfo('Response','Thanks for clicking the button.')

# Create an instance of the MyGUI class.
my_gui = MyGUI()