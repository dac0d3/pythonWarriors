
from tkinter import *
from tkinter import messagebox
import customtkinter

from chef import Chef
from runner import Runner 

chefUsername = 'u'
chefPassword = 'p'

runUsername = 'u'
runPassword = 'p'


'''
Class Name: EmployeeSignin

Date: 4/21/2024

Programmer's name: Diego Carbajal

Class Description: 

Important Functions: 
'''


class EmployeeSingIn(Toplevel):
    
    def __init__(self,parent):
        super().__init__(parent)
        
        self.title('Python Parlor Employee')
        self.geometry('1400x500')
        self.config(bg = '#d9472a')
        
        self.chefButton = customtkinter.CTkButton(self,text = 'Chef Sign In',command = self.chefSign,bg_color='#d9472a',fg_color='black')
        self.chefButton.pack()
        
        self.runnerButton = customtkinter.CTkButton(self,text = 'Runner Sign In',command = self.runnerSign,bg_color='#d9472a',fg_color='black')
        self.runnerButton.pack()
        
        self.backButton = customtkinter.CTkButton(self,text = '<',command = self.goBack,bg_color='#d9472a',fg_color='black')
        self.backButton.pack(pady = 50)
        
  
    def chefSign(self):
        ChefSignIn(self)
        self.forget(self)
           
    def runnerSign(self):
        RunnerSignIn(self)
        self.forget(self)
        
    def goBack(self):
        self.forget(self)   
    
      
      
      
        
'''
Class Name: ChefSignin

Date: 4/21/2024

Programmer's name: Diego Carbajal

Class Description:

Important Functions: 
'''
              
        
class ChefSignIn(Toplevel):
    
    def __init__(self,parent):
        super().__init__(parent)
        
        self.geometry('1400x500')
        self.title('Chef Sign In')
        self.config(bg = '#d9472a')
        
        self.user = customtkinter.CTkLabel(self,text = 'Enter Username: ' )
        self.user.grid(row =1,column = 1)
        
        self.entry1= Entry(self)
        self.entry1= customtkinter.CTkEntry(self,bg_color='#d9472a',fg_color='black')
        self.entry1.grid(row = 1,column = 2)
        
        self.passw = customtkinter.CTkLabel(self,text = 'Enter Password: ' )
        self.passw.grid(row =2,column = 1)
        
        self.entry2 = Entry(self)
        self.entry2= customtkinter.CTkEntry(self,bg_color='#d9472a',fg_color='black')
        self.entry2.grid(row = 2,column = 2)
        
        self.submit = customtkinter.CTkButton(self,text = "Submit",command = self.checkInfo,bg_color='#d9472a',fg_color='black')
        self.submit.grid(row = 3,column = 2)
        
        self.returnButton = customtkinter.CTkButton(self,text = 'Back',command = self.goBack,bg_color='#d9472a',fg_color='black')
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





'''
Class Name: RunnerSignin

Date: 4/21/2024

Programmer's name: Adrian Ramos

Class Description:

Important Functions: 


'''


class RunnerSignIn(Toplevel):
    
    def __init__(self,parent):
        super().__init__(parent)
        
        self.geometry('1400x500')
        self.title('Chef Sign In')
        self.config(bg = '#d9472a')
        
        self.user = customtkinter.CTkLabel(self,text = 'Enter Username: ' )
        self.user.grid(row =1,column = 1)
        
        self.entry1= Entry(self)
        self.entry1= customtkinter.CTkEntry(self,bg_color='#d9472a',fg_color='black')
        self.entry1.grid(row = 1,column = 2)
        
        self.passw = customtkinter.CTkLabel(self,text = 'Enter Password: ' )
        self.passw.grid(row =2,column = 1)
        
        self.entry2 = Entry(self)
        self.entry2= customtkinter.CTkEntry(self,bg_color='#d9472a',fg_color='black')
        self.entry2.grid(row = 2,column = 2)
        
        self.submit = customtkinter.CTkButton(self,text = "Submit",command = self.checkInfo,bg_color='#d9472a',fg_color='black')
        self.submit.grid(row = 3,column = 2)
        
        self.returnButton = customtkinter.CTkButton(self,text = 'Back',command = self.goBack,bg_color='#d9472a',fg_color='black')
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