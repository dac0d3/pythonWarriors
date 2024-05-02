
from tkinter import *
from tkinter import messagebox
import customtkinter

from chef import Chef
from runner import Runner 
#from main import Main

chefUsername = 'u'
chefPassword = 'p'

runUsername = 'u'
runPassword = 'p'


'''
Class Name: EmployeeSignin

Date: 4/21/2024

Programmer's name: Diego Carbajal

Class Description: This class will display a window that will let the actor choose the job/ shift he is working. 
His options are between the chef and the runner. Later he will need to verify his position with a username and password 
but in this screen all he does is click the position he wants to sign in for.

Important Functions: 

'chefSingIn' : 

'runnerSignIn' : 

'goBack' : 

'''


class EmployeeSingIn(Toplevel):
    
    def __init__(self,parent):
        super().__init__(parent)
        
        self.title('Python Parlor Employee')
        self.geometry('1000x500')
        self.config(bg = '#d9472a')
        
        self.chefButton = customtkinter.CTkButton(self,text = 'Chef Sign In',command = self.chefSign,bg_color='#d9472a',fg_color='black')
        self.chefButton.place(relx = 0.4,rely = 0.4,anchor = CENTER)
        
        self.runnerButton = customtkinter.CTkButton(self,text = 'Runner Sign In',command = self.runnerSign,bg_color='#d9472a',fg_color='black')
        self.runnerButton.place(relx = 0.5,rely = 0.4,anchor = CENTER)
        
        self.backButton = customtkinter.CTkButton(self,text = 'Back',
                                                  command = self.goBack,bg_color='#d9472a',
                                                  fg_color='black',height=10,
                                                  width = 10)
        self.backButton.place(relx = 0.1,rely = 0.9,anchor = CENTER)
        
  
    def chefSign(self):
        ChefSignIn(self)
        self.forget(self)
           
    def runnerSign(self):
        RunnerSignIn(self)
        self.forget(self)
        
    def goBack(self):
        self.withdraw()  
        from main import Main2
        Main2(self)
    
      
      
      
        
'''
Class Name: ChefSignin

Date: 4/21/2024

Programmer's name: Diego Carbajal

Class Description: When this class is called, it will promt the actor with a chef sign in window where he/she will
see two entry boxes, one for their username and one for their password. If their credentials are correct, then they will
move from the sign in screen to the home page will is called from the 'Chef' class. 

Important Functions: 

'checkCredentials' : is the funcion that holds the logic for the authentication of the chef sign in credentials.
It's a simple if statement that verifies that the username and password entered are correct. 
If so, the chef will get granted access to their homepage. If incorrect, there
will be a error message box letting the actor know that either their password or username were incorrect.

'goBack' : is simply a function that allows the user to go back to the previous screen and close the chef sign
in screen. 

'__init__' : This function is what creates the window and holds all the buttons and widgets dislayed in the GUI. 

'''
              
        
class ChefSignIn(Toplevel):
    
    def __init__(self,parent):
        super().__init__(parent)
        
        self.geometry('1000x500')
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
        self.withdraw()
        EmployeeSingIn(self)
        
        
        





'''
Class Name: RunnerSignin

Date: 4/21/2024

Programmer's name: Adrian Ramos

Class Description: When this class is called, it will promt the actor with a runner sign in window where he/she will
see two entry boxes, one for their username and one for their password. If their credentials are correct, then they will
move from the sign in screen to the home page will is called from the 'Runner' class. 

Important Functions: 

'checkCredentials' : is the funcion that holds the logic for the authentication of the runner sign in credentials.
It's a simple if statement that verifies that the username and password entered are correct. 
If so, the runner will get granted access to their homepage. If incorrect, there
will be a error message box letting the actor know that either their password or username were incorrect.

'goBack' : is simply a function that allows the user to go back to the previous screen and close the runner sign
in screen. 

'__init__' : This function is what creates the window and holds all the buttons and widgets dislayed in the GUI. 

'''


class RunnerSignIn(Toplevel):
    
    def __init__(self,parent):
        super().__init__(parent)
        
        self.geometry('1000x500')
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
        self.withdraw()
        EmployeeSingIn(self)