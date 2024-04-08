#name   #email   #confirm button takes to order file

#doc string documentation ?
from tkinter import *
from tkinter.tix import LabelEntry
from tkinter import messagebox
import openpyxl
from openpyxl import Workbook, load_workbook
from order import Order



    

book = load_workbook('customerTransactions.xlsx')
sheet = book.active



#windowCustomer = Tk()
#windowCustomer.geometry('1440x900')
#windowCustomer.title('Customer Registration')

    

cusID = sheet['A2'].value
cusID = int(cusID)
print('Customer ID: '+str(cusID))
    
class Customer(Toplevel):
    
    def __init__(self,parent):
        super().__init__(parent)
        
        self.geometry('1440x900')
        self.title('Customer Registration')
        
        self.nameVal = StringVar
        self.emailVal = StringVar

        #Heading 
        Label(self,text = "Customer Registration",font = 'ar 20 bold').grid(row = 0,column = 3)


        #Field Name
        self.name = Label(self,text = "Name")
        self.email = Label(self,text = "Email")

        self.name.grid(row = 1,column = 2)
        self.email.grid(row = 2,column = 2)


        #Creating Entry Field
        self.nameEntry = Entry(self,textvariable=self.nameVal)
        self.emailEntry = Entry(self,textvariable=self.emailVal)


        #Packing Entry Fields
        self.nameEntry.grid(row = 1,column = 3)
        self.emailEntry.grid(row = 2,column = 3)

        #Submit Button
        self.checkoutButton = Button(self,text = 'Submit',command = self.getVals)
        self.checkoutButton.grid(row = 7,column = 3)
        
        
            
       
    # gets values for name and email from customer when confirm button is clicked 
    def getVals(self):
        
        if self.nameEntry.get() and self.emailEntry.get():
            name = self.nameEntry.get()     
            email = self.emailEntry.get()
            #self.nameEntry.config(state = DISABLED)
            #self.emailEntry.config(state = DISABLED)
            
            sheet['B'+str(cusID)].value = name               # stores name in excel 
            sheet['C'+str(cusID)].value = email              # stores email in excel
            book.save('customerTransactions.xlsx')
            
            print("Name:", name)
            print("Email:", email)
        
            Order(self)         # srats order in order class
            self.forget(self)   # hides customer sign in for next customer 
            
            
        else:
            messagebox.showwarning('Error',"You missed an entry!")
        
        
        
    
        
    
        #windowCustomer.destroy()
        #print(nameVal,emailVal)
        
    




