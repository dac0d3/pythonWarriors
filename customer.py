
from tkinter import *
from tkinter.tix import LabelEntry
from tkinter import messagebox
import customtkinter
from PIL import ImageTk,Image
import ttkbootstrap as tb

import openpyxl
from openpyxl import Workbook, load_workbook

from updateTransaction import *

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
       
        
        self.geometry('1440x500')   #900
        self.title('Customer Registration')
        self.config(bg = '#d9472a')
        
        
        self.nameVal = StringVar
        self.emailVal = StringVar


        #Heading 
        #Label(self,text = "Customer Registration",font = 'ar 45 bold',bg = '#d9472a').place(relx = 0.105,rely = 0.065,anchor = W,fg = 'black')
        self.custRegTitle = customtkinter.CTkLabel(self,text = "Enter your information below",font = ('arial',30,'bold'),bg_color = '#d9472a',fg_color='#d9472a',text_color='#31120c',
                                                   height=40)
        self.custRegTitle.place(relx = 0.1,rely = 0.05,anchor = W)


        #Field Name
        self.name = customtkinter.CTkLabel(self,text = "Name: ",bg_color='#d9472a',font = ('arial',15))
        self.email = customtkinter.CTkLabel(self,text = "Email: ",bg_color = '#d9472a',font = ('arial',15))

        self.name.place(relx = 0.1,rely = 0.2,anchor = W)
        self.email.place(relx = 0.1,rely = 0.3,anchor = W)


        #Creating Entry Field
        self.nameEntry = customtkinter.CTkEntry(self,border_width=0 ,bg_color='#d9472a',corner_radius=5,fg_color='#db7c6b')    #bg_color='#d9472a',corner_radius=10    ,textvariable=self.nameVal                                  
        self.emailEntry = customtkinter.CTkEntry(self, border_width=0,bg_color='#d9472a',corner_radius=5,fg_color='#db7c6b')       #,textvariable=self.emailVal


        #Packing Entry Fields
        self.nameEntry.place(relx = 0.1,rely = 0.25,anchor = W)
        self.emailEntry.place(relx = 0.1,rely = 0.35,anchor = W)


        #Submit Button
        self.submitButton = customtkinter.CTkButton(self,text = 'Submit',command = self.getVals,
                                                    corner_radius=10,bg_color='#d9472a',
                                                    hover_color='gray',fg_color='#31120c')
        self.submitButton.place(relx = 0.1,rely = 0.5,anchor = W)
        
            
       
    # gets values for name and email from customer when confirm button is clicked 
    def getVals(self):
        
        from order import Order
        
        cusID = getCusID()
        
        if self.nameEntry.get() and self.emailEntry.get():
            name = self.nameEntry.get()     
            email = self.emailEntry.get()
            
            
            saveValues(cusID,name,email)
            
            #print("Name:", name)
            #print("Email:", email)
        
            Order(self)         # strts order in order class
            self.forget(self)   # hides customer sign in for next customer 
             
        else:
            messagebox.showwarning('Error',"You missed an entry!")
        
