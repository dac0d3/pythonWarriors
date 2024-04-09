# provide menu 
# send order to receipt file
# get total from dictionary and sends it to revenue file
# sends customer to checkout file

# shows checkout screen, 


import openpyxl
from openpyxl import Workbook, load_workbook

from tkinter import *

from revenue import calculateTax
from updateInventory import *
from updateTransaction import *


#book = load_workbook('customerTransactions.xlsx')
#sheet = book.active


menu = ['CHEESE PIZZA','PEPPERONI PIZZA','HAWAIIAN PIZZA','MEAT LOVERS PIZZA']
menu_prices = {'CHEESE PIZZA':15,'PEPPERONI PIZZA':17,'HAWAIIAN PIZZA':16,'MEAT LOVERS PIZZA':19} 


numCheesePizza = IntVar
numPepperoniPizza = IntVar
numHawaiianPizza = IntVar
numMeatLoversPizza = IntVar





class Order(Toplevel):

    orderPass = 0
    
    
    def __init__(self,parent):
        super().__init__(parent)
        
        self.book = load_workbook('customerTransactions.xlsx')
        self.sheet = self.book.active
        
        self.geometry('1440x500') #900
        self.title('Order Screen')
        
        #entry for Cheese pizzas 
        self.entryCP = Entry(self)
        self.entryCP.grid(row = 1,column = 2)

        #entry for Pepperoni pizzas 
        self.entryPP = Entry(self)
        self.entryPP.grid(row = 3,column = 2)

        #entry for Hawaiian pizzas 
        self.entryHP = Entry(self)
        self.entryHP.grid(row = 5,column = 2)

        #entry for Meat Lovers pizzas 
        self.entryMP = Entry(self)
        self.entryMP.grid(row = 7,column = 2)
        
        
        
        # button that will get order and open window to checkout screen 
        self.checkoutButton = Button(self,text = "Checkout",command = self.getValues)
        self.checkoutButton.grid(row = 12,column = 1)
        
        self.CPlabel = Label(self,text = 'Cheese Pizza')
        self.CPlabel.grid(row = 1,column = 1)
        
        
        self.PPlabel = Label(self,text = 'Pepperoni Pizza')
        self.PPlabel.grid(row = 3,column = 1)
        
        
        self.HPlabel = Label(self,text = 'Hawaiian Pizza')
        self.HPlabel.grid(row = 5,column = 1)
        
        
        self.MPlabel = Label(self,text = 'Meat Lovers Pizza')
        self.MPlabel.grid(row = 7,column = 1)
        



    def getValues(self):

        cusID = getCusID()
        print ('Customer ID:' +str(cusID))

        total = 0
        order = []



        #Update number of cheese pizzas
        numCheesePizza = self.entryCP.get()

        if len(numCheesePizza)== 0:
            numCheesePizza = 0
            numCheesePizza = float(numCheesePizza)
        else:
            numCheesePizza = float(numCheesePizza)

        price1 = menu_prices['CHEESE PIZZA']                             #Finds price of pizza in menu
        priceWithTax1 = calculateTax(price1)                              #calculates tax
        priceWithTax1 = priceWithTax1 * numCheesePizza
        #print('Order:\nCheese Pizza: '+str(numCheesePizza)+'\nPrice: '+str(priceWithTax1))
        order.append(priceWithTax1)
        cheesePizza(numCheesePizza)
        #sheet['D'+str(cusID)].value = numCheesePizza



        #Update number of cheese pizzas
        numPepperoniPizza = self.entryPP.get()

        if len(numPepperoniPizza)==0:
            numPepperoniPizza = 0
            numPepperoniPizza = float(numPepperoniPizza)
        else:
            numPepperoniPizza = float(numPepperoniPizza)

        price2 = menu_prices['PEPPERONI PIZZA']                           #Finds price of pizza in menu
        priceWithTax2 = calculateTax(price2)                              #calculates tax 
        priceWithTax2 = numPepperoniPizza * priceWithTax2
        #print('Order:\nPepperoni Pizza: '+ str(numPepperoniPizza)+'\nPrice: '+str(priceWithTax2))
        order.append(priceWithTax2)
        pepperonniPizza(numPepperoniPizza)
        #sheet['E'+str(cusID)].value = numPepperoniPizza



        #update number of Hawaiian pizzas
        numHawaiianPizza = self.entryHP.get()

        if len(numHawaiianPizza)==0:
            numHawaiianPizza = 0
            numHawaiianPizza = float(numHawaiianPizza)
        else:
            numHawaiianPizza = float(numHawaiianPizza)

        price3 = menu_prices['HAWAIIAN PIZZA']                             #Finds price of pizza in menu
        priceWithTax3 = calculateTax(price3)                                #calculates tax
        priceWithTax3 = priceWithTax3 * numHawaiianPizza
        #print('Order:\nHawaiian Pizza: '+str(numHawaiianPizza)+'\nPrice: '+str(priceWithTax3))
        order.append(priceWithTax3)
        hawaiianPizza(numHawaiianPizza)
        #sheet['F'+str(cusID)].value = numHawaiianPizza



        #update nuumber of meat lovers pizzas
        numMeatLoversPizza = self.entryMP.get()                                 #Gets num of pizza from entry

        if len(numMeatLoversPizza)==0:
            numMeatLoversPizza = 0
            numMeatLoversPizza = float(numMeatLoversPizza)
        else:
            numMeatLoversPizza = float(numMeatLoversPizza) 

        price4 = menu_prices['MEAT LOVERS PIZZA']                            #Finds price of pizza in menu
        priceWithTax4 = calculateTax(price4)                                 #calculates tax
        priceWithTax4 = priceWithTax4 * numMeatLoversPizza
        #print('Order:\nMeat Lovers Pizza: '+str(numMeatLoversPizza)+'\nPrice: '+str(priceWithTax4))
        order.append(priceWithTax4)
        meatLoversPizza(numMeatLoversPizza)
        #sheet['G'+str(cusID)].value = numMeatLoversPizza



        for index in order:
            if total == 0:
                total = index
            else:
                total = total + index
                
        total = round(total,2)  # round total to 2 decimals 
       
        saveOrder(cusID,numCheesePizza,numPepperoniPizza,numHawaiianPizza,numMeatLoversPizza,total)
        
        
        #sheet['H'+str(cusID)].value = total
        #book.save('customerTransactions.xlsx')
        print(total)
        print(order)

        
       
        Checkout2(self)
        self.forget(self)
        
        #checkOrderPass(orderPass)
        
        
        
        
class Checkout2(Toplevel):
    
    
    def __init__(self,parent):
        super().__init__(parent)
        
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
        
        cusID = getCusID()               
        newCusID = updateCusID(cusID)

        sheet['A'+str(newCusID)].value = newCusID   # sets the order ID for next customer transaction and saves to excel
        book.save('customerTransactions.xlsx')
        # start new customer transaction

        self.destroy()
    
    

        
        










