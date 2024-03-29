
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
    
    

from customer import cusID      #gets the id and row for customer 

numCP = sheet['D'+str(cusID)].value   
numPP = sheet['E'+str(cusID)].value  
numHP = sheet['F'+str(cusID)].value  
numMP = sheet['G'+str(cusID)].value

print(numCP,numPP,numHP,numMP)  
















    
# label with pizza order  and   another label with number of pizzas 
label1 = Label(window2,text = 'Cheese Pizzas')    
label1.grid(row = 1,column = 1)  
    
label2 = Label(window2,text = "Pepperoni Pizzas")    
label2.grid(row = 2,column = 1)  
    
label3 = Label(window2,text = "Hawaiian Pizzas")    
label3.grid(row = 3,column = 1)  
    
label4 = Label(window2,text = "Meat Lovers Pizzas")    
label4.grid(row = 4,column = 1)  



def orderComplete():
    print('Order Submitted')
        
    # start new customer transaction
        
    window2.destroy()
    
checkoutButton = Button(window2,text = 'Complete Order',command = orderComplete )
checkoutButton.grid(row = 10,column=10)
        
       
    

    
        
        
        
window2.mainloop()
        
        
        
        
    
    
    
    
    
    
##################################################################################################################