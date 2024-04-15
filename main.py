from tkinter import *
from customtkinter import *

from managerSignIn import ManagerSignIn
from employeeSingIn import EmployeeSingIn

class Main(Tk):
    
    def __init__(self):
        super().__init__()
        
        self.config(bg = '#387FC8')
        self.geometry('1400x500')
        self.title('Main')
        
        self.optionFrame = Frame(self,bg = '#F3B552',padx = 20,pady = 30)
        #self.optionFrame.size('50x50')
        self.optionFrame.pack(padx = 1 ,pady = 60)
    
        self.button1 = Button(self.optionFrame,text = 'Employee Sign-in',command = self.employeeSign,background = 'blue')
        #self.button1.config(font =('Arial',50))
        self.button1.pack()
        #self.button1.place(rely = 0.5,relx = 0.16,anchor =CENTER)
        
        self.button2 = Button(self.optionFrame,text = 'Manager Sign-in',command = self.managerSign)
        #self.button2.config(font =('Arial',50) )
        self.button2.pack()
        #self.button2.place(rely =0.35,relx = 0.161,anchor =CENTER)
        
        #self.closeButton = Button(self,text = 'X',command = self.closeScreen)
        #self.closeButton.place(anchor = NW)
        #self.closeButton.config()

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

