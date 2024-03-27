# provide menu 
# send order to receipt file
# get total from dictionary and sends it to revenue file
# sends customer to checkout file




from tkinter import *
from revenue import calculateTax
#from customer import nameVal,emailVal





menu = ['CHEESE PIZZA','PEPPERONI PIZZA','HAWAIIAN PIZZA','MEAT LOVERS PIZZA']
menu_prices = {'CHEESE PIZZA':15,'PEPPERONI PIZZA':17,'HAWAIIAN PIZZA':16,'MEAT LOVERS PIZZA':19} 


numCheesePizza = IntVar
numPepperoniPizza = IntVar
numHawaiianPizza = IntVar
numMeatLoversPizza = IntVar


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



##################################################################################################################



#This class has the informaiton of the menu that displays to the customer 
class Order_Menu:
    
    def goToCheckout ():
        
        total = 0
        order = []
        
        
        
        #Update number of cheese pizzas
        numCheesePizza = entryCP.get()
        
        if len(numCheesePizza)== 0:
            numCheesePizza = 0
            numCheesePizza = float(numCheesePizza)
        else:
            numCheesePizza = float(numCheesePizza)
                                                                       
        price1 = menu_prices['CHEESE PIZZA']                             #Finds price of pizza in menu
        priceWithTax1 = calculateTax(price1)                              #calculates tax
        priceWithTax1 = priceWithTax1 * numCheesePizza
        #print('Order:\nCheese Pizza: '+str(numCheesePizza)+'\nPrice: '+str(priceWithTax))
        order.append(priceWithTax1)
        
        
        
        
        
        #Update number of cheese pizzas
        numPepperoniPizza = entryPP.get()
        
        if len(numPepperoniPizza)==0:
            numPepperoniPizza = 0
            numPepperoniPizza = float(numPepperoniPizza)
        else:
            numPepperoniPizza = float(numPepperoniPizza)
               
        price2 = menu_prices['PEPPERONI PIZZA']                           #Finds price of pizza in menu
        priceWithTax2 = calculateTax(price2)                              #calculates tax 
        priceWithTax2 = numPepperoniPizza * priceWithTax2
        #print('Order:\nPepperoni Pizza: '+ str(numPepperoniPizza)+'\nPrice: '+str(priceWithTax))
        order.append(priceWithTax2)
        
        
        
        
        
        #update number of Hawaiian pizzas
        numHawaiianPizza = entryHP.get()
        
        if len(numHawaiianPizza)==0:
            numHawaiianPizza = 0
            numHawaiianPizza = float(numHawaiianPizza)
        else:
            numHawaiianPizza = float(numHawaiianPizza)
            
        price3 = menu_prices['HAWAIIAN PIZZA']                             #Finds price of pizza in menu
        priceWithTax3 = calculateTax(price3)                                #calculates tax
        priceWithTax3 = priceWithTax3 * numHawaiianPizza
        #print('Order:\nHawaiian Pizza: '+str(numHawaiianPizza)+'\nPrice: '+str(priceWithTax))
        order.append(priceWithTax3)
        
        
        
        
        
        #update nuumber of meat lovers pizzas
        numMeatLoversPizza = entryMP.get()                                 #Gets num of pizza from entry
       
        if len(numMeatLoversPizza)==0:
            numMeatLoversPizza = 0
            numMeatLoversPizza = float(numMeatLoversPizza)
        else:
            numMeatLoversPizza = float(numMeatLoversPizza) 
            
        price4 = menu_prices['MEAT LOVERS PIZZA']                            #Finds price of pizza in menu
        priceWithTax4 = calculateTax(price4)                                 #calculates tax
        priceWithTax4 = priceWithTax4 * numMeatLoversPizza
        #print('Order:\nMeat Lovers Pizza: '+str(numMeatLoversPizza)+'\nPrice: '+str(priceWithTax))
        order.append(priceWithTax4)
        
        
        
        
        
        for index in order:
            if total == 0:
                total = index
            else:
                total = total + index
            
        print(total)
        print(order)
        
        window.destroy()
        
        #after this, Order_menu class ends and Checkout class precedes
        
        from checkout import Checkout
        order1 = Checkout(numCheesePizza,numPepperoniPizza,numHawaiianPizza,numMeatLoversPizza,total)
        
               
        
        
    # button that will get order and open window to checkout screen 
    checkoutButton = Button(window,text = "Checkout",command = goToCheckout)
    checkoutButton.grid(row = 12,column = 1)



    CPlabel = Label(window,text = 'Cheese Pizza')
    CPlabel.grid(row = 1,column = 1)
    
    
    PPlabel = Label(window,text = 'Pepperoni Pizza')
    PPlabel.grid(row = 3,column = 1)
    
        
    HPlabel = Label(window,text = 'Hawaiian Pizza')
    HPlabel.grid(row = 5,column = 1)
    

    MPlabel = Label(window,text = 'Meat Lovers Pizza')
    MPlabel.grid(row = 7,column = 1)
    

    

    window.mainloop()




##################################################################################################################


