import tkinter
class MyGUI:
    def __init__(self):
    # Create the main window widget.
        self.main_window = tkinter.Tk()
        # Create a Label widget containing the
        # text 'Hello World!'
        self.label1 = tkinter.Label(self.main_window, text='Hello World!')
        self.label2 = tkinter.Label(self.main_window,text='This is my GUI program.')
        # Call the Label widget's pack method.
        # self.label1.pack()
        # self.label2.pack()
        self.label1.pack(side = 'left')
        self.label2.pack(side = 'left')
        # Enter the tkinter main loop.
        tkinter.mainloop()
        # Create an instance of the MyGUI class.

my_gui = MyGUI()