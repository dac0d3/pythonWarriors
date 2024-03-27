# provide menu 
# send order to receipt file
# get total from dictionary and sends it to revenue file
# sends customer to confirmOrder file

# display receipt from receipt file 
# confirm button = (sends order to chef) && (updates inventory on excel)
# starts a new customer transaction in customer file


from tkinter import *
from revenue import calculateTax
from updateInventory import *
#from customer import nameVal,emailVal



menu = ['CHEESE PIZZA','PEPPERONI PIZZA','HAWAIIAN PIZZA','MEAT LOVERS PIZZA']
menu_prices = {'CHEESE PIZZA':15,'PEPPERONI PIZZA':17,'HAWAIIAN PIZZA':16,'MEAT LOVERS PIZZA':19} 


numCheesePizza = IntVar
numPepperoniPizza = IntVar
numHawaiianPizza = IntVar
numMeatLoversPizza = IntVar

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
entryHP = Entry(window)
entryHP.grid(row = 5,column = 2)

#entry for Meat Lovers pizzas 
entryMP = Entry(window)
entryMP.grid(row = 7,column = 2)


 
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
        #after this, Order_Menu class ends and Checkout class precedes
        
    # button that will get order and open window to checkout screen 
    checkoutButton = Button(window,text = "Checkout",command = goToCheckout)
    checkoutButton.grid(row = 12,column = 1)




    #Update number of cheese pizzas
    def updateCP():
        numCheesePizza = entryCP.get()
        numCheesePizza = int(numCheesePizza)
        price = menu_prices['CHEESE PIZZA']                             #Finds price of pizza in menu
        priceWithTax = calculateTax(price)                              #calculates tax
        print('Order:\nCheese Pizza: '+
              str(numCheesePizza)+'\nPrice: '+str(priceWithTax))
        #cheesePizza(numCheesePizza)
        
    CPlabel = Label(window,text = 'Cheese Pizza')
    CPlabel.grid(row = 1,column = 1)
    
    CPbutton = Button(window,text = 'Add to Order',command = updateCP)
    CPbutton.grid(row = 2 ,column = 2)
    
    
    
    
    
    #Update number of pepperoni pizzas
    def updatePP():
        numPepperoniPizza = entryPP.get()
        price = menu_prices['PEPPERONI PIZZA']                           #Finds price of pizza in menu
        priceWithTax = calculateTax(price)                               #calculates tax
        print('Order:\nPepperoni Pizza: '+
              str(numPepperoniPizza)+'\nPrice: '+str(priceWithTax))
        
    
    PPlabel = Label(window,text = 'Pepperoni Pizza')
    PPlabel.grid(row = 3,column = 1)
    
    PPbutton = Button(window,text = 'Add to Order',command = updatePP)
    PPbutton.grid(row =4,column = 2)
    
    
    
    
     
    #Update number of hawaiian pizzas
    def updateHP():
        numHawaiianPizza = entryHP.get()
        price = menu_prices['HAWAIIAN PIZZA']                             #Finds price of pizza in menu
        priceWithTax = calculateTax(price)                                #calculates tax
        print('Order:\nHawaiian Pizza: '+
              str(numHawaiianPizza)+'\nPrice: '+str(priceWithTax))
        
    HPlabel = Label(window,text = 'Hawaiian Pizza')
    HPlabel.grid(row = 5,column = 1)
    
    HPbutton = Button(window,text = 'Add to Order',command = updateHP)
    HPbutton.grid(row =6,column = 2)
    
    
    
    
    #Update number of meat lovers pizza
    def updateMP():
        numMeatLoversPizza = entryMP.get()                                 #Gets num of pizza from entry
        price = menu_prices['MEAT LOVERS PIZZA']                           #Finds price of pizza in menu
        priceWithTax = calculateTax(price)                                 #calculates tax
        print('Order:\nMeat Lovers Pizza: '+
              str(numMeatLoversPizza)+'\nPrice: '+str(priceWithTax))

    MPlabel = Label(window,text = 'Meat Lovers Pizza')
    MPlabel.grid(row = 7,column = 1)
    
    MPbutton = Button(window,text = 'Add to Order',command = updateMP)
    MPbutton.grid(row = 8,column = 2)
    

    window.mainloop()





##################################################################################################################




window2 = Tk()
window2.geometry('1440x900')
window2.title('Checkout')


class Checkout():
    
    
        
    def orderComplete():
        print('Order Submitted')
        
        window2.destroy()
    
    
    checkoutButton = Button(window2,text = 'Complete Order',command = orderComplete )
    checkoutButton.pack()
        
        
    window.mainloop()
        
        
        
        
    
    
    
    
    
    
##################################################################################################################