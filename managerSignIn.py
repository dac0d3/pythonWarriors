from tkinter import *

username = 'username'
password = 'password'



class ManagerSignIn(Tk):
    def __init__(self):
        super().__init__()
        
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
        pass
    
    
    
    print('Manager Signed in')
    
    
    
run = ManagerSignIn()
run.mainloop()