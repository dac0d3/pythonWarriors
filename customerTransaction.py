

import openpyxl
from openpyxl import Workbook, load_workbook

from tkinter import *

from updateInventory import *
from customer import Customer
from updateTransaction import *



#book = load_workbook('customerTransactions.xlsx')
#sheet = book.active


#sheet['A2'].value = 2
cusID = sheet['A2'].value
cusID = int(cusID)
book.save('customerTransactions.xlsx')

print('Customer ID: '+str(cusID))


class CustomerTransaction(Tk):
    
    def __init__(self,):
        super().__init__()
        
        self.title('Customer Transaction')  # Set title using method, not property
        self.geometry('1440x500')

        self.button1 = Button(self,text = 'Start Transaction',command = self.startTransaction)
        self.button1.pack()
        
        self.button2 = Button(self,text = 'Stop Taking Orders',command = self.stopTransactions)
        self.button2.pack(pady = 20)
        
        
    def stopTransactions(self):
        
        # open new window to input manager credentials and then if correct kiosk will close 
        
        self.destroy() 
        
         
        
    def startTransaction(self):
        addOneCust()
        Customer(self)
        
        
    
       
run = CustomerTransaction()
run.mainloop()
