from tkinter import *
from customtkinter import *

from managerSignIn import ManagerSignIn
from employeeSingIn import EmployeeSingIn

class Main(Tk):
    
    def __init__(self):
        super().__init__()
        
        self.geometry('1400x500')
        self.title('Main')
        
        self.button1 = Button(self,text = 'Employee Sign-in',command = self.employeeSign)
        self.button1.pack()
        
        self.button2 = Button(self,text = 'Manager Sign-in',command = self.managerSign)
        self.button2.pack()
        
        self.closeButton = Button(self,text = 'Close',command = self.closeScreen)
        self.closeButton.pack()

    def employeeSign(self):
        EmployeeSingIn(self)
        #self.destroy()
    
    def managerSign(self):
        ManagerSignIn(self)
        #self.forget(self)

    def closeScreen(self):
        self.destroy()


run = Main()
run.mainloop()

