from tkinter import *
from customtkinter import *

from customerTransaction import CustomerTransaction
from updateTransaction import *


class Kiosk(Tk):
    def __init__(self):
        super().__init__()
        
        self.geometry('1400x500')
        self.title('Open Kiosk')
        
        self.button1 = Button(self,text = 'Open Kiosk',command = self.startCustT)
        self.button1.pack()
        
        #place(anchor = CENTER)
        
        self.button2 = Button(self,text = 'Close Kiosk',command = self.closeKiosk)
        self.button2.pack()
        
        
        
    def startCustT(self):
        CustomerTransaction(self)
        #self.destroy()
        
    def closeKiosk(self):
        self.destroy() 
        resetCusID()
        print("Kiosk is now closed.")  
        
        
run = Kiosk()
run.mainloop()