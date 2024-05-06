
from tkinter import *
from tkinter.tix import LabelEntry
from tkinter import messagebox
import customtkinter
from PIL import ImageTk,Image
import ttkbootstrap as tb

import openpyxl
from openpyxl import Workbook, load_workbook

from updateTransaction import *
from emailConfirm import emailConf

book = load_workbook('customerTransactions.xlsx')
sheet = book.active
    
    
'''
Class Name: Customer
Documentation Date: 04/21/24
Prog. Name: Diego Carbajal

Class Descripion: This class is called after the customer decides to start their transaction. This class will display a 
GUI showing two entry boxes, one for the name and email for the customer. Once the customer has filled in their 
information, they can move on to the next phase of their order by clicking the Submit button. 

Important Functions: 

'__init__' : This function is what creates the window and holds all the buttons and widgets dislayed in the GUI. 

'getValues' : This function gets the customers name and email when the confirm button is clicked. The two string values
along with the customers ID number are then sent to the 'saveValues' function in the 'updateTransaction' file. And if the 
customer left an entry box empty, an error message box will display asking them to make sure they fill out every entry. 

'''
    
    
class Customer(Toplevel):
    
   
    
    def __init__(self,parent):
        super().__init__(parent)
       
        
        self.geometry('1100x600')
        self.title('Customer Registration')
        self.config(bg = '#bf3c22')
        
        
        self.nameVal = StringVar
        self.emailVal = StringVar


        # Frame for everything in window
        self.infoFrame = Frame(self,bg = '#FFE6D8',pady = 100,padx = 100,highlightbackground="#31120c", highlightcolor="#31120c", highlightthickness=3,bd = 0) #highlightbackground="#d9472a"
        self.infoFrame.place(relx = 0.5,rely = 0.5,anchor = CENTER)
        
        
        #Heading 
        #Label(self,text = "Customer Registration",font = 'ar 45 bold',bg = '#d9472a').place(relx = 0.105,rely = 0.065,anchor = W,fg = 'black')
        self.custRegTitle = customtkinter.CTkLabel(self.infoFrame,text = "Enter your information below",font = ('arial',30,'bold'),bg_color = '#FFE6D8',fg_color='#FFE6D8',text_color='#31120c',
                                                   height=40)
        self.custRegTitle.grid(row = 0,column= 0,columnspan = 2,pady = 20)


        #Field Name
        self.name = customtkinter.CTkLabel(self.infoFrame,text = "Name: ",bg_color='#FFE6D8',font = ('arial',15),text_color='#31120c')
        self.email = customtkinter.CTkLabel(self.infoFrame,text = "Email: ",bg_color = '#FFE6D8',font = ('arial',15),text_color='#31120c')

        self.name.grid(row = 1,column= 0,pady = 2,columnspan = 2)
        self.email.grid(row = 3,column= 0,pady = 2,columnspan = 2)


        #Creating Entry Field
        self.nameEntry = customtkinter.CTkEntry(self.infoFrame,border_width=0 ,bg_color='#FFE6D8',corner_radius=5,fg_color='#db7c6b',)    #bg_color='#d9472a',corner_radius=10    ,textvariable=self.nameVal                                  
        self.emailEntry = customtkinter.CTkEntry(self.infoFrame, border_width=0,bg_color='#FFE6D8',corner_radius=5,fg_color='#db7c6b',)       #,textvariable=self.emailVal


        #Packing Entry Fields
        self.nameEntry.grid(row = 2,column= 0,pady = 2,columnspan = 2)
        self.emailEntry.grid(row = 4,column= 0,pady = 2,columnspan = 2)


        #Submit Button
        self.submitButton = customtkinter.CTkButton(self.infoFrame,text = 'Submit',command = self.getVals,
                                                    corner_radius=10,bg_color='#FFE6D8',
                                                    hover_color='gray',fg_color='#31120c')
        #self.submitButton.place(relx = 0.1,rely = 0.5,anchor = W)
        self.submitButton.grid(row = 5,column= 0,columnspan = 2,pady = 30)
        
        
        
        
            
       
    # gets values for name and email from customer when confirm button is clicked 
    def getVals(self):
        
        from order import Order
        
        cusID = getCusID()
        
        if self.nameEntry.get() and self.emailEntry.get():
            name = self.nameEntry.get()     
            email = self.emailEntry.get()
            
            # Checks validity of email and send email to verify customer 
            emailCheck = emailConf(email)
            
            if name.isalpha() == True:
                if emailCheck == True: 
                    saveValues(cusID,name,email)

                        #print("Name:", name)
                        #print("Email:", email)

                    Order(self)         # strts order in order class
                    self.forget(self)   # hides customer sign in for next customer 
                else:
                    messagebox.showwarning('Error',"Your email is not valid")
            else:
                messagebox.showwarning('Error',"Your name can only contain letters")
             
        else:
            messagebox.showwarning('Error',"You missed an entry!")
     
     
     
'''
if email.find('@my.csun.edu')!= -1 or email.find('@gmail.com')!= -1 or email.find('@icloud.com')!= -1 :
                    
                        
else:
    messagebox.showwarning('Error',"Enter your csun, gmail, or icloud email")
    '''