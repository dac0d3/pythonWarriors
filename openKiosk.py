# currently skipping open kiosk class and going straight to customer placing order srceen


from tkinter import *
import customtkinter
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



class CustomerTransaction(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title('Customer Transaction')  
        self.geometry('1440x500')
        self.config(bg = '#bf3c22')
 
        self.logo = Image.open('pythonLogo.png')
        self.resized = self.logo.resize((510,400))
        self.logoNew = ImageTk.PhotoImage(self.resized)
        
        self.photoLabel = Label(self, image = self.logoNew,bg ='#bf3c22')
        self.photoLabel.place(relx = 0.5,rely = 0.5,anchor = CENTER)
        
        
        self.button1 = customtkinter.CTkButton(self,text = 'Start your Order',command = self.startTransaction,bg_color ='#bf3c22',
                                                font= ('arial',17),corner_radius=10,fg_color = '#31120c')
        
        self.button1.place(relx = 0.51,rely = 0.6, anchor = CENTER)
        
        
    def stopTransactions(self):
        
        # open new window to input manager credentials and then if correct kiosk will close 
        ManagerClose(self)
        #self.forget(self) 
        
         
    def startTransaction(self):
        addOneCust()
        Customer(self)
        #self.forget(self)
        
    def closeKiosk(self):
        self.destroy()
        


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

        
    
run = CustomerTransaction()
run.mainloop()