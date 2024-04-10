from tkinter import *

from managerSignIn import ManagerSignIn

class Main(Tk):
    
    def __init__(self):
        super().__init__()
        
        self.geometry('1400x500')
        self.title('Main')
        
        self.button1 = Button(self,text = 'Start Cus Order',command = self.startCustT)
        self.button1.pack()
        
        self.button2 = Button(self,text = 'Start Employee Sign',command = self.employeeSign)
        self.button2.pack()
        
        self.button3 = Button(self,text = 'Start Manager Sign',command = self.managerSign)
        self.button3.pack()
        

    def startCustT(self):
        from customerTransaction import CustomerTransaction
        #self.destroy()
    
    def employeeSign(self):
        from employeeSingIn import EmployeeSingIn
        #self.destroy()
    
    def managerSign(self):
        ManagerSignIn(self)
        #self.forget(self)




run = Main()
run.mainloop()

