# provide menu 
# send order to receipt file
# get total from dictionary and sends it to revenue file
# sends customer to confirmOrder file

# display receipt from receipt file 
# confirm button = (sends order to chef) && (updates inventory on excel)
# starts a new customer transaction in customer file


from tkinter import *
from tkinter import BOTH,END,LEFT
from revenue import calculateTax
#from customer import nameVal,emailVal



menu = ['CHEESE PIZZA','PEPPERONI PIZZA','HAWAIIAN PIZZA','MEAT LOVERS PIZZA']
menu_prices = {'CHEESE PIZZA':15,'PEPPERONNI PIZZA':17,'HAWAIIAN PIZZA':16,'MEAT LOVERS PIZZA':19} 




##################################################################################################################



window = Tk()
window.geometry('1440x900')
window.title('Order Screen')

#entry for Cheese pizzas 
entryCP = Entry(window)
entryCP.grid(row = 1,column = 2)

#entry for Pepperoni pizzas 
entryPP = Entry(window)
entryPP.grid(row = 3,column = 2)

#entry for Hawaiian pizzas 
entryCP = Entry(window)
entryCP.grid(row = 5,column = 2)


 
totalList = []      #list that holds the prices of the customer selection with tax 


#This class has the informaiton of the menu that displays to the customer 
class Order_Menu:
    
    def goToCheckout ():
        
        total = 0
        order = []
    
        # inserts selected items in order[]
        
        # loop to calc tax for each item
        
        # this loop calculates total of order with tax 
        
            
        window.destroy()
        #after this, Checkout class precedes
        

    # button that will get order and open window to checkout screen 
    checkoutButton = Button(window,text = "Checkout",command = goToCheckout)
    checkoutButton.grid(row = 12,column = 2)



    #Update number of cheese pizzas
    def updateCP():
        numCheesePizza = entryCP.get()
        
    CPlabel = Label(window,text = 'Cheese Pizza')
    CPlabel.grid(row = 1,column = 1)
    
    CPbutton = Button(window,text = 'Add to Order',command = updateCP)
    CPbutton.grid(row =2,column = 1)
    
    
    
    #Update number of pepperoni pizzas
    def updatePP():
        pass
    
    PPlabel = Label(window,text = 'Pepperoni Pizza')
    PPlabel.grid(row = 3,column = 1)
    
    PPbutton = Button(window,text = 'Add to Order',command = updatePP)
    PPbutton.grid(row =4,column = 1)
    
    
     
    #Update number of hawaiian pizzas
    def updateHP():
        pass
    
    HPlabel = Label(window,text = 'Hawaiian Pizza')
    HPlabel.grid(row = 5,column = 1)
    
    HPbutton = Button(window,text = 'Add to Order',command = updateHP)
    HPbutton.grid(row =6,column = 1)
    

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