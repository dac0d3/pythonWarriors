# provide menu 
# send order to receipt file
# get total from dictionary and sends it to revenue file
# sends customer to confirmOrder file

# display receipt from receipt file 
# confirm button = (sends order to chef) && (updates inventory on excel)
# starts a new customer transaction in customer file
from tkinter import *

menu = ['CHEESE PIZZA','PEPPERONI PIZZA',]
menu_prices = {'CHEESE PIZZA':15,'PEPPERONNI PIZZA':17} # needs full menu and prices 

orderId = None
pizzaOrder = None
total = None



window = Tk()
window.geometry('500x500')
menubox = Listbox(window,font = 'Constantia',width = 15,selectmode = MULTIPLE)
menubox.pack()
#listbox.grid(row = 1,column=1)
#listbox.anchor()
    
class Order_Menu:
    
    def checkout ():
        
        order = []
    
        for index in menubox.curselection():
            order.insert(index,menubox.get(index))
        
        for index in order:
            total(index)
            print(index)
            
        # function to open new window here 
        
        
    def calculateTotal(x):
        pass
          
        

    # Menu Items
    menubox.insert(1,'Cheese Pizza')
    menubox.insert(2,'Meat Lovers Pizza')
    menubox.insert(3,'Pepperoni Pizza')
    menubox.insert(4,'Hawaiian Pizza')

    # make size of menu same as number of items
    menubox.config(height = menubox.size())

    # button that will get order and open window to checkout screen 
    checkoutButton = Button(window,text = "Checkout",command = checkout)
    checkoutButton.pack()

    window.mainloop()


class Checkout:
    pass