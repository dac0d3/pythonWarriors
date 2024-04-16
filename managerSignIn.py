from tkinter import *
from tkinter import messagebox
import customtkinter

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
        self.config(bg = '#d9472a')
        
        self.user = customtkinter.CTkLabel(self,text = 'Enter Username: ' )
        self.user.place(relx = 0.1,rely = 0.2,anchor = W)
        
        self.entry1= customtkinter.CTkEntry(self)
        self.entry1.place(relx = 0.2,rely = 0.2,anchor = W)
        
        self.passw = customtkinter.CTkLabel(self,text = 'Enter Password: ' )
        self.passw.place(relx = 0.1,rely = 0.3,anchor = W)
        
        self.entry2 = customtkinter.CTkEntry(self)
        self.entry2.place(relx = 0.2,rely = 0.3,anchor = W)
        
        self.submit = customtkinter.CTkButton(self,text = "Submit",command = self.checkCredentials)
        self.submit.place(relx = 0.2,rely = 0.4,anchor = W)
    
        self.returnButton = customtkinter.CTkButton(self,text = 'Back',command = self.goBack)
        self.returnButton.place(relx = 0.1,rely = 0.4,anchor = W)
    
    
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
        
        rev = round(rev,2)
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