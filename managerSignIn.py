from tkinter import *
from tkinter import messagebox

from updateInventory import *
from updateTransaction import *

username = 'u'
password = 'p'



class ManagerSignIn(Toplevel):
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
    
    
    def checkCredentials(self):
        usName = self.entry1.get()
        passW = self.entry2.get()
        
        if usName == username and passW == password:
            print('Manager Signed in!')
            ManagerHomePage(self)
            self.forget(self)
        else:
            messagebox.showwarning('Error',"Incorrect password or username")
    
    
    
    

class ManagerHomePage(Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        
        self.title('Manager HomePage')
        self.geometry('1400x500')

        self.button1 = Button(self,text = 'Restock Inventory',command = self.resetInventory)
        self.button1.pack()
        
        self.button2 = Button(self,text = 'Reset Transactions', command = self.resetTrans)
        self.button2.pack()
    
    
    
    def resetInventory(self):
        restockInventory()
        print('Inventory has been restocked!')
        
    def resetTrans(self):
        resetTransactions()
        
        
#run = ManagerSignIn()
#run.mainloop()