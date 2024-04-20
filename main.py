from tkinter import *
import customtkinter
from PIL import ImageTk,Image


from managerSignIn import ManagerSignIn
from employeeSingIn import EmployeeSingIn
from chef import Chef

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

