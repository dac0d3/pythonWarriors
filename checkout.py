
# display receipt from receipt file 
# confirm button = (sends order to chef) && (updates inventory on excel)
# starts a new customer transaction in customer file

from tkinter import *
from updateInventory import *

window2 = Tk()
window2.geometry('1440x900')
window2.title('Checkout')
    
class Checkout():
    
    

    def orderComplete():
        print('Order Submitted')
        
        # call receipt to store values in excel
        # call update inventory to change excel values 
        # send order to chef
        
        window2.destroy()
    
    checkoutButton = Button(window2,text = 'Complete Order',command = orderComplete )
    checkoutButton.pack()
        
        
    # label with pizza order  and   another label with number of pizzas 
        
        
        
        
        
    window2.mainloop()
        
        
        
        
    
    
    
    
    
    
##################################################################################################################