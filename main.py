from tkinter import *


class Main(Tk):
    
    def __init__(self):
        super().__init__()
        
        self.geometry('1400x500')
        
        self.button1 = Button(self,text = 'Start Cus Order',command = self.startCustT)
        self.button1.pack()
        
        self.button2 = Button(self,text = 'Start Employee Sign',command = self.employeeSign)
        self.button2.pack()
        
        self.button3 = Button(self,text = 'Start Manager Sign',command = self.managerSign)
        self.button3.pack()
        

    def startCustT(self):
        from customerTransaction import CustomerTransaction
        #self.forget()
    
    def employeeSign(self):
        from employeeSingIn import EmployeeSingIn
        #self.forget()
    
    def managerSign(self):
        from managerSignIn import ManagerSignIn
        #self.forget()




run = Main()
run.mainloop()

