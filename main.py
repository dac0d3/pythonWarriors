from tkinter import *
import customtkinter
from PIL import ImageTk,Image

from managerSignIn import ManagerSignIn
from employeeSingIn import EmployeeSingIn
from chef import Chef

'''


Class Name: main
Documentation Date: 04/20/24
Prog. Name: Diego Carbajal

Class Descripion: 
This class is what starts the Managerial sign in. It opens a window which prompts the user to 
sign into their designated role whether that be as an employee or a manager. This main class will remain running even
when the actor has signed in. Because of this, the actor will be able to come back to this page at any time. 

Important Functions: 

There are three functions in this class.

The 'managerSign' function is the function called if the actor wants to 
sign in as a manger. This function calls the 'ManagerSignIn' class which opens a new window for the user to input 
their credentials. 

The 'employeeSign' function is the function called if the actor wants to 
sign in as an employee, either chef or runner. This function calls the 'EmployeeSignIn' class which opens a new window 
for the user to input their credentials. 

The 'closeScreen' function is pretty self explanatory, it simply closes the screen and ends the program. 



'''





class Main(Tk):
    
    def __init__(self):
        super().__init__()
        
        
        self.geometry('1400x500')
        self.title('Main')
        self.config(bg = '#d9472a') 
        
        self.logo = Image.open('pythonLogo.png')
        self.resized = self.logo.resize((510,400))
        self.logoNew = ImageTk.PhotoImage(self.resized)
        
        self.photoLabel = Label(self, image = self.logoNew,bg ='#d9472a')
        self.photoLabel.place(relx = 0.5,rely = 0.5,anchor = CENTER)



        self.employeeButton = customtkinter.CTkButton(self,text = 'Employee Sign-in',command = self.employeeSign,bg_color= '#d9472a',
                                               fg_color='black',height = 40,width=20)
        self.employeeButton.place(relx = 0.41,rely = 0.6,anchor = W)
        
        
        self.managerButton = customtkinter.CTkButton(self,text = 'Manager Sign-in',command = self.managerSign,bg_color= '#d9472a',
                                               fg_color='black',height = 40,width=20)
        self.managerButton.place(relx = 0.61,rely = 0.6,anchor = E)
        

    def employeeSign(self):
        EmployeeSingIn(self)
        #self.destroy()
    
    def managerSign(self):
        ManagerSignIn(self)
        #self.forget(self)

    def closeScreen(self):
        self.destroy()


run = Main()
run.mainloop()

