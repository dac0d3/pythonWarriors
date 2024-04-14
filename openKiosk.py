from tkinter import *
from customtkinter import *
from tkinter import messagebox

#from customerTransaction import CustomerTransaction

import openpyxl
from openpyxl import Workbook, load_workbook

from updateInventory import *
from customer import Customer
from updateTransaction import *
from managerClose import ManagerClose
#from kiosk import ManagerOpenClose


#sheet['A2'].value = 2
cusID = sheet['A2'].value
cusID = int(cusID)
book.save('customerTransactions.xlsx')

print('Customer ID: '+str(cusID))



#book = load_workbook('customerTransactions.xlsx')
#sheet = book.active


class CustomerTransaction(Toplevel):
    
    def __init__(self,parent):
        super().__init__(parent)
        
        self.title('Customer Transaction')  # Set title using method, not property
        self.geometry('1440x500')

        self.button1 = Button(self,text = 'Start Transaction',command = self.startTransaction)
        self.button1.pack()
        
        self.button2 = Button(self,text = 'Exit',command = self.stopTransactions)
        self.button2.pack(pady = 20)
        
        
    def stopTransactions(self):
        
        # open new window to input manager credentials and then if correct kiosk will close 
        ManagerClose(self)
        self.forget(self) 
        
         
        
    def startTransaction(self):
        addOneCust()
        Customer(self)
        #self.forget(self)
        


class OpenKiosk(Tk):
    def __init__(self):
        super().__init__()
        
        self.geometry('1400x500')
        self.title('Open Kiosk')
        
        self.button1 = Button(self,text = 'Open Kiosk',command = self.startCustT)
        self.button1.pack()
        
        #place(anchor = CENTER)
        
        #self.button2 = Button(self,text = 'Close Kiosk',command = self.closeKiosk)
        #self.button2.pack()
        
        
        
    def startCustT(self):
        CustomerTransaction(self)
        #self.forget(self)
        
    #def closeKiosk(self):
     #   self.destroy() 
      #  resetCusID()
       # print("Kiosk is now closed.")  
        

  
       
#run = CustomerTransaction()
#run.mainloop()
    
run = OpenKiosk()
run.mainloop()