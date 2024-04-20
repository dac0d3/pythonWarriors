from tkinter import *
from tkinter import messagebox
import customtkinter
from PIL import ImageTk,Image

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
        
        self.logo = Image.open('pythonLogo.png')
        self.resized = self.logo.resize((510,400))
        self.logoNew = ImageTk.PhotoImage(self.resized)
        
        self.photoLabel = Label(self, image = self.logoNew,bg ='#d9472a')
        self.photoLabel.place(relx = 0.62,rely = 0.43,anchor = CENTER)
        
        
        
        #Heading 
        self.managerTitle = customtkinter.CTkLabel(self,text = "Manager Sign-In",font = ('arial',30),bg_color = '#d9472a')
        self.managerTitle.place(relx = 0.1,rely = 0.05,anchor = W)
        
        
        self.user = customtkinter.CTkLabel(self,text = 'Enter Username: ' )
        self.user.place(relx = 0.1,rely = 0.2,anchor = W)
        
        self.entry1= customtkinter.CTkEntry(self,bg_color='#d9472a',fg_color='black')
        self.entry1.place(relx = 0.2,rely = 0.2,anchor = W)
        
        self.passw = customtkinter.CTkLabel(self,text = 'Enter Password: ' )
        self.passw.place(relx = 0.1,rely = 0.3,anchor = W)
        
        self.entry2 = customtkinter.CTkEntry(self,bg_color='#d9472a',fg_color='black')
        self.entry2.place(relx = 0.2,rely = 0.3,anchor = W)
        
        self.submit = customtkinter.CTkButton(self,text = "Submit",command = self.checkCredentials,
                                              bg_color='#d9472a',fg_color='black')
        self.submit.place(relx = 0.2,rely = 0.4,anchor = W)
    
        self.returnButton = customtkinter.CTkButton(self,text = 'Back',command = self.goBack,
                                                    bg_color='#d9472a',fg_color='black',height = 10,width = 10)
        self.returnButton.place(relx = 0.1,rely = 0.9,anchor = SW)
    
    
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
        self.config(bg = '#d9472a')


        self.logo = Image.open('pythonLogo.png')
        self.resized = self.logo.resize((310,200))
        self.logoNew = ImageTk.PhotoImage(self.resized)
        
        self.photoLabel = Label(self, image = self.logoNew,bg ='#d9472a')
        self.photoLabel.place(relx = 0.76,rely = 0.2,anchor = CENTER)




        self.button1 = customtkinter.CTkButton(self,text = 'Restock Inventory',command = self.resetInventory,
                                               bg_color='#d9472a',fg_color='black')
        self.button1.place(relx = 0.5,rely = 0.4,anchor = W)
        
        self.button2 = customtkinter.CTkButton(self,text = 'Reset Transactions', command = self.resetTrans,
                                               bg_color='#d9472a',fg_color='black')
        self.button2.place(relx = 0.5,rely = 0.5,anchor = W)
        
        self.button4 = customtkinter.CTkButton(self,text = 'Exit',command = self.closeWindow,
                                               bg_color='#d9472a',fg_color='black')
        self.button4.place(relx = 0.5,rely = 0.6,anchor = W)
        

        
        rev = getRevenue()
        
        rev = round(rev,2)
        self.label = customtkinter.CTkLabel(self,text = 'Current Revenue: $'+str(rev),
                                            bg_color='#d9472a',fg_color='black')
        self.label.place(relx = 0.5,rely = 0.7,anchor = W)
        
        
    def resetInventory(self):
        restockInventory()
        print('Inventory has been restocked!')
        
    def resetTrans(self):
        resetTransactions()
        
    def closeWindow(self):
        self.forget(self)
    
