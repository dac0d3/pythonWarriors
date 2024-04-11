from tkinter import *
from tkinter import messagebox

from chef import Chef
from runner import Runner 

chefUsername = 'u'
chefPassword = 'p'

runUsername = 'u'
runPassword = 'p'


class EmployeeSingIn(Toplevel):
    
    def __init__(self,parent):
        super().__init__(parent)
        
        self.title('Python Parlor Employee')
        self.geometry('1400x500')
        
        self.chefButton = Button(self,text = 'Chef Sign In',command = self.chefSign)
        self.chefButton.pack()
        
        self.runnerButton = Button(self,text = 'Runner Sign In',command = self.runnerSign)
        self.runnerButton.pack()
        
        self.backButton = Button(self,text = '<',command = self.goBack)
        self.backButton.pack(pady = 50)
        
  
    def chefSign(self):
        ChefSignIn(self)
        self.forget(self)
           
    def runnerSign(self):
        RunnerSignIn(self)
        self.forget(self)
        
    def goBack(self):
        self.forget(self)   
    
        
        
        
        
        
        
class ChefSignIn(Toplevel):
    
    def __init__(self,parent):
        super().__init__(parent)
        
        self.geometry('1400x500')
        self.title('Chef Sign In')
        
        self.user = Label(self,text = 'Enter Username: ' )
        self.user.grid(row =1,column = 1)
        
        self.entry1= Entry(self)
        self.entry1.grid(row = 1,column = 2)
        
        self.passw = Label(self,text = 'Enter Password: ' )
        self.passw.grid(row =2,column = 1)
        
        self.entry2 = Entry(self)
        self.entry2.grid(row = 2,column = 2)
        
        self.submit = Button(self,text = "Submit",command = self.checkInfo)
        self.submit.grid(row = 3,column = 2)
        
        self.returnButton = Button(self,text = 'Back',command = self.goBack)
        self.returnButton.grid(row = 10,column = 1)
    
    
    def checkInfo(self):
        usName = self.entry1.get()
        passW = self.entry2.get()
        
        if usName == chefUsername and passW == chefPassword:
            print('Chef Signed in!')
            Chef(self)
            self.forget(self)
        else:
            messagebox.showwarning('Error',"Incorrect password or username")


    def goBack(self):
        self.forget(self)











class RunnerSignIn(Toplevel):
    
    def __init__(self,parent):
        super().__init__(parent)
        
        self.geometry('1400x500')
        self.title('Runner Sign In')
        
        self.user = Label(self,text = 'Enter Username: ' )
        self.user.grid(row =1,column = 1)
        
        self.entry1= Entry(self)
        self.entry1.grid(row = 1,column = 2)
        
        self.passw = Label(self,text = 'Enter Password: ' )
        self.passw.grid(row =2,column = 1)
        
        self.entry2 = Entry(self)
        self.entry2.grid(row = 2,column = 2)
        
        self.submit = Button(self,text = "Submit",command = self.checkInfo)
        self.submit.grid(row = 3,column = 2)
        
        self.returnButton = Button(self,text = 'Back',command = self.goBack)
        self.returnButton.grid(row = 10,column = 1)
    
    
    
    def checkInfo(self):
        usName = self.entry1.get()
        passW = self.entry2.get()
        
        if usName == runUsername and passW == runPassword:
            print('Runner Signed in!')
            Runner(self)
            self.forget(self)
        else:
            messagebox.showwarning('Error',"Incorrect password or username")

    def goBack(self):
        self.forget(self)