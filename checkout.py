
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



heading = Label(window2,text = "Order",font = 'ar 20 bold').grid(row = 0,column = 1)


    
# label with pizza order and another label with number of pizzas 

label1 = Label(window2,text = 'Cheese Pizzas: ')    
label1.grid(row = 1,column = 1)  
label1Num = Label(window2,text = str(numCP))    
label1Num.grid(row = 1,column = 2)
    
label2 = Label(window2,text = "Pepperoni Pizzas: ")    
label2.grid(row = 2,column = 1)  
label2Num = Label(window2,text = str(numPP))    
label2Num.grid(row = 2,column = 2)
    
label3 = Label(window2,text = "Hawaiian Pizzas: ")    
label3.grid(row = 3,column = 1) 
label3Num = Label(window2,text = str(numHP))    
label3Num.grid(row = 3,column = 2) 
    
label4 = Label(window2,text = "Meat Lovers Pizzas: ")    
label4.grid(row = 4,column = 1)  
label4Num = Label(window2,text = str(numMP))    
label4Num.grid(row = 4,column = 2)



def orderComplete():
    print('Order Submitted')
    
    from customer import cusID                  # sets the order ID for next customer transaction and saves to excel
    cusID = int(cusID)
    cusID = cusID + 1
    sheet['A'+str(cusID)].value = cusID
    
    book.save('customerTransactions.xlsx')
    # start new customer transaction
        
    
    window2.destroy()
    
    
checkoutButton = Button(window2,text = 'Complete Order',command = orderComplete )
checkoutButton.grid(row = 10,column=10)
        
       
    

    
        
        

 
window2.mainloop()
        
        
        

        
    
    
    
    
    
    
##################################################################################################################