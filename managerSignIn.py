from tkinter import *
from tkinter import messagebox

from updateInventory import *
from updateTransaction import *
from revenue import *

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
    
        self.returnButton = Button(self,text = 'Back',command = self.goBack)
        self.returnButton.grid(row = 10,column = 1)
    
    
    def checkCredentials(self):
        usName = self.entry1.get()
        passW = self.entry2.get()
        
        if usName == username and passW == password:
            print('Manager Signed in!')
            ManagerHomePage(self)
            self.forget(self)
            
        else:
            messagebox.showwarning('Error',"Incorrect password or username")
    
    
    def goBack(self):
        self.forget(self)
    

class ManagerHomePage(Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        
        self.title('Manager HomePage')
        self.geometry('1400x500')

        self.button1 = Button(self,text = 'Restock Inventory',command = self.resetInventory)
        self.button1.pack()
        
        self.button2 = Button(self,text = 'Reset Transactions', command = self.resetTrans)
        self.button2.pack()

        #self.button3 = Button(self,text = 'Check Revenue',command = self.checkRev)
        #self.button3.pack()
        
        self.button4 = Button(self,text = 'Exit',command = self.closeWindow)
        self.button4.pack()
        
        #self.button1 = Button(self,text = 'Return',command = self.backToHP)
        #self.button1.pack()
        
        rev = getRevenue()
        
        self.label = Label(self,text = 'Current Revenue: '+str(rev))
        self.label.pack()
        
        
    def resetInventory(self):
        restockInventory()
        print('Inventory has been restocked!')
        
    def resetTrans(self):
        resetTransactions()
        
    def closeWindow(self):
        self.forget(self)
    
    #def checkRev(self):
     #   CheckRevenue(self)
      #  self.forget(self)
        
        
    
    
#class CheckRevenue(Toplevel):
#    def __init__(self,parent):
#        super().__init__(parent)
#        
#        # get revenue from revenue file 
#        
#        self.geometry('1400x900')
#        self.title('Check Revenue')
#        
#        
#        
#        
#    def backToHP(self):
#        ManagerHomePage(self)
#        self.forget(self)


        
#run = ManagerSignIn()
#run.mainloop()