from tkinter import *
from tkinter import messagebox

from updateTransaction import *
from customer import Customer


username = 'u'
password = 'p'


class ManagerClose(Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        
        self.geometry('1400x500')
        self.title('Manager Sign In')
        
        
        self.user = Label(self,text = 'Enter Username: ' )
        self.user.grid(row =1,column = 1)
        
        self.entry1= Entry(self)
        self.entry1.grid(row = 1,column = 2)
        
        self.passw = Label(self,text = 'Enter Password: ' )
        self.passw.grid(row =2,column = 1)
        
        self.entry2 = Entry(self)
        self.entry2.grid(row = 2,column = 2)
        
        self.submit = Button(self,text = "Submit",command = self.checkCredentials)
        self.submit.grid(row = 3,column = 2)
        
       # self.transactionButton = Button(self,text = 'Continue Transactions',command = self.continueTrans)
        #self.transactionButton.grid(row = 10,column = 1)
        
    #def continueTrans(self):
     #   Customer(self)
      #  self.forget(self)
     
        
    def checkCredentials(self):
        usName = self.entry1.get()
        passW = self.entry2.get()
        
        if usName == username and passW == password:
            print('Manager Signed in!')
            CloseKiosk(self)
            self.forget(self)
            
        else:
            messagebox.showwarning('Error',"Incorrect password or username")


class CloseKiosk(Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        
        self.geometry('1400x500')
        self.title('Close Kiosk')
        
        #place(anchor = CENTER)
        
        self.button2 = Button(self,text = 'Close Kiosk',command = self.closeKiosk)
        self.button2.pack()
        
        
        
        
    def closeKiosk(self):
        self.destroy() 
        resetCusID()
        print("Kiosk is now closed.")  
        
    