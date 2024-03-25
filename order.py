# provide menu 
# send order to receipt file
# get total from dictionary and sends it to revenue file
# sends customer to confirmOrder file

# display receipt from receipt file 
# confirm button = (sends order to chef) && (updates inventory on excel)
# starts a new customer transaction in customer file


from tkinter import *
from revenue import calculateTax
#from customer import nameVal,emailVal



menu = ['CHEESE PIZZA','PEPPERONI PIZZA','HAWAIIAN PIZZA','MEAT LOVERS PIZZA']
menu_prices = {'CHEESE PIZZA':15,'PEPPERONNI PIZZA':17,'HAWAIIAN PIZZA':16,'MEAT LOVERS PIZZA':19} 




##################################################################################################################



window = Tk()
window.geometry('1440x900')
window.title('Order Screen')

menubox = Listbox(window,font = 'Constantia',width = 15,selectmode = MULTIPLE)
menubox.pack()
#listbox.grid(row = 1,column=1)
#listbox.anchor()
 
totalList = []      #list that holds the prices of the customer selection with tax 


#This class has the informaiton of the menu that displays to the customer 
class Order_Menu:
    
    def goToCheckout ():
        
        total = 0
        order = []
    
        for index in menubox.curselection():
            order.insert(index,menubox.get(index))  # inserts selected items in order[]
            
        for index in order:
            item = index.upper()                #capitalizes option to find it in menu
            i = menu_prices[item]               #get price of item in menu 
            itemWithTax = calculateTax(i)       #sends item to calculateTax
            totalList.append(itemWithTax)       #adds new price to totalList[]
            
            #print(i)                            #prints price of item
        
        
        # this loop calculates total of order with tax 
        for index in totalList:
            if (total != 0):
                total = total + index
            else:
                total = index
        
        print(total)    # print price of total order 
            
        window.destroy()
        #after this, Checkout class precedes
        
          
    # Menu Items
    menubox.insert(1,'Cheese Pizza')
    menubox.insert(2,'Meat Lovers Pizza')
    menubox.insert(3,'Pepperonni Pizza')
    menubox.insert(4,'Hawaiian Pizza')

    # make size of menu same as number of items
    menubox.config(height = menubox.size())

    # button that will get order and open window to checkout screen 
    checkoutButton = Button(window,text = "Checkout",command = goToCheckout)
    checkoutButton.pack()

    window.mainloop()





##################################################################################################################




window2 = Tk()
window2.geometry('1440x900')
window2.title('Checkout')


class Checkout():
        
   
        
    def orderComplete():
        
        
        window2.destroy()
    
    
    checkoutButton = Button(window2,text = 'Complete Order',command = orderComplete )
    checkoutButton.pack()
        
        
    window.mainloop()
        
        
        
        
    print('Order Submitted')
    
    
    
    
    
##################################################################################################################