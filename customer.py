#name   #email   #confirm button takes to order file

#doc string documentation ?
from tkinter import *
from tkinter.tix import LabelEntry
import openpyxl
from openpyxl import Workbook, load_workbook

#from main import Main,cusID
    

book = load_workbook('customerTransactions.xlsx')
sheet = book.active


window = Tk()
window.geometry('1440x900')
window.title('Customer Registration')
    

cusID = sheet['A2'].value
cusID = int(cusID)
print('Customer ID: '+str(cusID))
    
class Customer:

    def __init__(self,window):
        
        nameVal = StringVar
        emailVal = StringVar
        
        #Heading 
        Label(window,text = "Customer Registration",font = 'ar 20 bold').grid(row = 0,column = 3)
        
        
        #Field Name
        self.name = Label(window,text = "Name")
        self.email = Label(window,text = "Email")
        
        self.name.grid(row = 1,column = 2)
        self.email.grid(row = 2,column = 2)
        
        
        #Creating Entry Field
        self.nameEntry = Entry(window,textvariable=nameVal)
        self.emailEntry = Entry(window,textvariable=emailVal)
    
    
        #Packing Entry Fields
        self.nameEntry.grid(row = 1,column = 3)
        self.emailEntry.grid(row = 2,column = 3)
        
        #Submit Button
        self.checkoutButton = Button(window,text = 'Submit',command = self.getVals)
        self.checkoutButton.grid(row = 7,column = 3)
        
        
        
        
    
    # gets values for name and email from customer when confirm button is clicked 
    def getVals(self):
        
        self.nameVal = self.nameEntry.get()     #nameEntry
        self.emailVal = self.emailEntry.get()
        self.nameEntry.config(state = DISABLED)
        self.emailEntry.config(state = DISABLED)
    
        sheet['B'+str(cusID)].value = self.nameVal               # stores name in excel 
        sheet['C'+str(cusID)].value = self.emailVal              # stores email in excel
        book.save('customerTransactions.xlsx')
    
        #print(nameVal,emailVal)
        window.destroy()            #close window here 
        #import order #  <-- call class for order here
    


    
    
    
customer = Customer(window) 

  
window.mainloop()

