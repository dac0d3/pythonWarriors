
# display receipt from receipt file 
# confirm button = (sends order to chef) && (updates inventory on excel)
# starts a new customer transaction in customer file

from tkinter import *
from updateInventory import *
import openpyxl
from openpyxl import Workbook, load_workbook


book = load_workbook('customerTransactions.xlsx')       # get values to show on display for customer from excel
sheet = book.active


window2 = Tk()
window2.geometry('1440x900')
window2.title('Checkout')
    




def orderComplete():
    print('Order Submitted')
        
    # call receipt to store values in excel 
    # call update inventory to change excel values 
    # send order to chef
        
    window2.destroy()
    
checkoutButton = Button(window2,text = 'Complete Order',command = orderComplete )
checkoutButton.grid(row = 10,column=10)
        
       
    
# label with pizza order  and   another label with number of pizzas 
label1 = Label(window2,text = 'label 1')    
label1.grid(row = 1,column = 1)  
    
label2 = Label(window2,text = "label 2")    
label2.grid(row = 2,column = 1)  
    
label3 = Label(window2,text = "label 3")    
label3.grid(row = 3,column = 1)  
    
label4 = Label(window2,text = "label 4")    
label4.grid(row = 4,column = 1)  
    
        
        
        
window2.mainloop()
        
        
        
        
    
    
    
    
    
    
##################################################################################################################