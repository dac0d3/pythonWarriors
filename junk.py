











#this file is for refrence if anything goes wrong
# is not being used!!!!



















import openpyxl
from openpyxl import Workbook, load_workbook

from tkinter import *

from updateInventory import *
from customer import Customer
from updateTransaction import *
from managerClose import ManagerClose
#from kiosk import ManagerOpenClose



#book = load_workbook('customerTransactions.xlsx')
#sheet = book.active


#sheet['A2'].value = 2
cusID = sheet['A2'].value
cusID = int(cusID)
book.save('customerTransactions.xlsx')

print('Customer ID: '+str(cusID))


class CustomerTransaction(Toplevel):
    
    def __init__(self,):
        super().__init__()
        
        self.title('Customer Transaction')  # Set title using method, not property
        self.geometry('1440x500')

        self.button1 = Button(self,text = 'Start Transaction',command = self.startTransaction)
        self.button1.pack()
        
        self.button2 = Button(self,text = '<',command = self.stopTransactions)
        self.button2.pack(pady = 20)
        
        
    def stopTransactions(self):
        
        # open new window to input manager credentials and then if correct kiosk will close 
        ManagerClose(self)
        self.forget(self) 
        
         
        
    def startTransaction(self):
        addOneCust()
        Customer(self)
        
        
    
       
#run = CustomerTransaction()
#run.mainloop()


        
        
    'This used to be in the open KioskClass, has been moved to this junk file'
          
   #def stopTransactions(self):
   #    
   #    # open new window to input manager credentials and then if correct kiosk will close 
   #    ManagerClose(self)
   #    #self.forget(self) 
   #    
   #     
   #
   #    
   #def closeKiosk(self):
   #    self.destroy()
   #    

   #
   # class OpenKiosk(customtkinter.CTk):
   #    def __init__(self):
   #        super().__init__()
   #        
   #        
   #        
   #        self.geometry('1400x500')
   #        self.title('Open Kiosk')
   #        self.config(bg = '#d9472a')
   # 
   #        
   #        self.logo = Image.open('pythonLogo.png')
   #        self.resized = self.logo.resize((500,400))
   #        self.logoNew = ImageTk.PhotoImage(self.resized)
   #        
   #        
   #        self.photoLabel = Label(self, image = self.logoNew,compound = 'bottom', bg = '#d9472a')
   #        self.photoLabel.place(relx = 0.5,rely = 0.5)
   #        
   #        
   #        
   #        self.button1 = customtkinter.CTkButton(self,text = 'Open Kiosk',command = self.startCustT,font =('Montserrat',17),
   #                                                corner_radius=10,hover_color = 'gray',bg_color='#d9472a',
   #                                                fg_color='black')
   #        
   #        self.button1.place(relx = 0.51,rely = 0.6, anchor = CENTER)
   #        
   #        
   #        
   #        
   #    def startCustT(self):
   #        CustomerTransaction(self)