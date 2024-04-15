#name   #email   #confirm button takes to order file

#doc string documentation ?
from tkinter import *
from tkinter.tix import LabelEntry
from tkinter import messagebox
import customtkinter
from PIL import ImageTk,Image
import ttkbootstrap as tb

import openpyxl
from openpyxl import Workbook, load_workbook

from order import Order
from updateTransaction import *

book = load_workbook('customerTransactions.xlsx')
sheet = book.active
    

    
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
        Label(self,text = "Customer Registration",font = 'ar 45 bold',bg = 'black').place(relx = 0.1,rely = 0.06,anchor = W)
        


        #Field Name
        self.name = Label(self,text = "Name",bg='#d9472a',font = ('arial',15))
        self.email = Label(self,text = "Email",bg = '#d9472a',font = ('arial',15))

        self.name.place(relx = 0.1,rely = 0.2,anchor = W)
        self.email.place(relx = 0.1,rely = 0.3,anchor = W)


        #Creating Entry Field
        self.nameEntry = Entry(self,textvariable=self.nameVal,bd=0 ,bg ='black')    #bg_color='#d9472a',corner_radius=10                                      
        self.emailEntry = Entry(self,textvariable=self.emailVal, bd=0,bg='black' )


        #Packing Entry Fields
        self.nameEntry.place(relx = 0.1,rely = 0.25,anchor = W)
        self.emailEntry.place(relx = 0.1,rely = 0.35,anchor = W)


        #Submit Button
        self.submitButton = customtkinter.CTkButton(self,text = 'Submit',command = self.getVals,
                                                    corner_radius=10,bg_color='#d9472a',
                                                    hover_color='gray',fg_color='black')
        self.submitButton.place(relx = 0.1,rely = 0.5,anchor = W)
        
            
       
    # gets values for name and email from customer when confirm button is clicked 
    def getVals(self):
        
        cusID = getCusID()
        
        if self.nameEntry.get() and self.emailEntry.get():
            name = self.nameEntry.get()     
            email = self.emailEntry.get()
            #self.nameEntry.config(state = DISABLED)
            #self.emailEntry.config(state = DISABLED)
            
            saveValues(cusID,name,email)
            
            #print("Name:", name)
            #print("Email:", email)
        
            Order(self)         # srats order in order class
            self.forget(self)   # hides customer sign in for next customer 
             
        else:
            messagebox.showwarning('Error',"You missed an entry!")
        

        
        
        
        