
from tkinter import *
import customtkinter
from tkinter import messagebox
from PIL import ImageTk,Image
import ttkbootstrap as tb


import openpyxl
from openpyxl import Workbook, load_workbook

from updateInventory import *
from updateTransaction import *




'''

Class Name: CustomerTransaction
Documentation Date: 04/21/24
Prog. Name: Diego Carbajal

Class Descripion: This class is the main loop for the customer transaction, it 
creates the first window a customer would see when they want to place an order. The window shows the
retaurant logo and a button which lets the customer know that they need to click it in order to start their order. 


Important Functions: 

'__init__' : This function is what creates the window and holds all the buttons and widgets dislayed in the GUI. 

'startTransaction' : This function is called when the customer clicks on the button to start their transaction. 
And this function will call the 'Customer' class and also the 'addOneCust' method in the 'updateTransaction' file. 


'''



class CustomerTransaction(Toplevel): #customtkinter.CTk
    
    def __init__(self,):
        super().__init__()
        
        #parent.destroy()
        
        self.title('Customer Transaction')  
        # make function to get resolution so that it adjusts to each window 
        
        self.geometry('500x300')
        self.config(bg = '#bf3c22')
 
        self.logo = Image.open('pythonLogo.png')
        self.resized = self.logo.resize((510,400))
        self.logoNew = ImageTk.PhotoImage(self.resized)
        
        self.photoLabel = Label(self, image = self.logoNew,bg ='#bf3c22')
        self.photoLabel.place(relx = 0.5,rely = 0.5,anchor = CENTER)
        
        
        self.startButton = customtkinter.CTkButton(self,text = 'Start your Order',command = self.startTransaction,bg_color ='#bf3c22',
                                                font= ('arial',17),corner_radius=10,fg_color = '#31120c')
        
        self.startButton.place(relx = 0.51,rely = 0.6, anchor = CENTER)
        
    def startTransaction(self):
        
        from customer import Customer
        addOneCust()
        Customer(self)
       
        self.forget(self)
        #self.destroy()
        
           
           
def start():
    global run
    
    run = CustomerTransaction()
    run.mainloop()
    
def stopAndRun():
      
    run.forget(run)
    start()
    
start() 
    
    

