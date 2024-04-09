
# display receipt from receipt file 
# confirm button = (sends order to chef) && (updates inventory on excel)
# starts a new customer transaction in customer file

from tkinter import *
from updateInventory import *
import openpyxl
from openpyxl import Workbook, load_workbook
from updateTransaction import *


book = load_workbook('customerTransactions.xlsx')       # get values to show on display for customer from excel
sheet = book.active





class Checkout(Toplevel):
    
    
    
    def __init__(self):
        super().__init__()
        
        cusID = getCusID()    #gets the id and row for customer 
        print(cusID)
        
        self.geometry('1440x500')
        self.title('Checkout')

        numCP = sheet['D'+str(cusID)].value   
        numPP = sheet['E'+str(cusID)].value  
        numHP = sheet['F'+str(cusID)].value  
        numMP = sheet['G'+str(cusID)].value

        print(numCP,numPP,numHP,numMP)  


        self.heading = Label(self,text = "Order",font = 'ar 20 bold').grid(row = 0,column = 1)



        # label with pizza order and another label with number of pizzas 

        self.label1 = Label(self,text = 'Cheese Pizzas: ')    
        self.label1.grid(row = 1,column = 1)  
        self.label1Num = Label(self,text = str(numCP))    
        self.label1Num.grid(row = 1,column = 2)

        self.label2 = Label(self,text = "Pepperoni Pizzas: ")    
        self.label2.grid(row = 2,column = 1)  
        self.label2Num = Label(self,text = str(numPP))    
        self.label2Num.grid(row = 2,column = 2)

        self.label3 = Label(self,text = "Hawaiian Pizzas: ")    
        self.label3.grid(row = 3,column = 1) 
        self.label3Num = Label(self,text = str(numHP))    
        self.label3Num.grid(row = 3,column = 2) 

        self.label4 = Label(self,text = "Meat Lovers Pizzas: ")    
        self.label4.grid(row = 4,column = 1)  
        self.label4Num = Label(self,text = str(numMP))    
        self.label4Num.grid(row = 4,column = 2)


        self.checkoutButton = Button(self,text = 'Complete Order',command = self.orderComplete )
        self.checkoutButton.grid(row = 10,column=10)


    def orderComplete(self):
        print('Order Submitted')

        cusID = getCusID()               # sets the order ID for next customer transaction and saves to excel
        newCusID = updateCusID(cusID)
        
        sheet['A'+str(cusID)].value = newCusID

        book.save('customerTransactions.xlsx')
        # start new customer transaction

        

        self.destroy()


   
        
        

        
    
    
    
    
    
    
##################################################################################################################