from tkinter import *
from customtkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import ttkbootstrap as tb


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
        
 
        self.logo = Image.open('pythonLogo.png')
        self.resized = self.logo.resize((510,400))
        self.logoNew = ImageTk.PhotoImage(self.resized)
        
        self.photoLabel = Label(self, image = self.logoNew)
        self.photoLabel.pack()
        
        
        
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
        self.config(bg = '#d9472a')
        
        #self.frame = Frame(self,bg = '#d9472a')
        #self.frame.place(x = 100,y = 0)
        
        self.logo = Image.open('pythonLogo.png')
        self.resized = self.logo.resize((500,400))
        self.logoNew = ImageTk.PhotoImage(self.resized)
        
        
        self.photoLabel = Label(self, image = self.logoNew,compound = 'bottom', bg = '#d9472a')
        #self.photoLabel.grid(row = 1,column = 1)
        self.photoLabel.place(relx = 0.5,rely = 0.5,anchor = CENTER)
        
        self.button1 = Button(self,text = 'Open Kiosk',command = self.startCustT,font =('Montserrat',17),activebackground = '#d9472a',
                              bd = 0)
        #self.button1.grid(row = 2,column = 1)
        self.button1.place(relx = 0.51,rely = 0.6, anchor = CENTER)
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