

import openpyxl
from openpyxl import Workbook, load_workbook
from tkinter import *
from updateInventory import *

from customer import Customer
from checkout import Checkout


book = load_workbook('customerTransactions.xlsx')
sheet = book.active


#cusID = sheet['A2'].value
#cusID = int(cusID)
#print('Customer ID: '+str(cusID))


class CustomerTransaction(Tk):
    
    def __init__(self):
        super().__init__()
        
        self.title('Main1')  # Set title using method, not property
        self.geometry('1440x500')

        self.button1 = Button(self,text = 'Start Transaction',command = self.startTransaction)
        self.button1.pack()
        
        self.button2 = Button(self,text = 'Close Kiosk',command = self.closeKiosk)
        self.button2.pack(pady = 20)
        
        
        #This will be a manager exclusive method call
        self.button3 = Button(self,text = 'Restock Inventory',command = self.resetInventory)
        self.button3.pack()
        
    def closeKiosk(self):
        self.destroy() 
        print("Kiosk is now closed.")  
         
        
    def startTransaction(self):
        Customer(self)
        #Checkout(self)
    
    #if statement here 

    def resetInventory(self):
        restockInventory()
        print('Inventory has been restocked!')


        
run = CustomerTransaction()
run.mainloop()
