# provide menu 
# send order to receipt file
# get total from dictionary and sends it to revenue file
# sends customer to checkout file

# shows checkout screen, 


import openpyxl
from openpyxl import Workbook, load_workbook

from tkinter import *
import customtkinter
from PIL import ImageTk,Image
import ttkbootstrap as tb

from revenue import *
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
        self.config(bg = '#d9472a') 
        
        
        
        
        # Displays images for Cheese pizza 
        self.cheesePizzaIm = Image.open('360_F_26257008_Amvaw8kdz8KViXR1Gc3fNgl2sfubDV8E.webp')
        self.resized = self.cheesePizzaIm.resize((100,100))
        self.cheesePizzaImNew = ImageTk.PhotoImage(self.resized)
        self.cheesePhotoLabel = Label(self,image = self.cheesePizzaImNew,bg ='#d9472a')
        self.cheesePhotoLabel.place(relx = 0.8,rely = 0.7,anchor = E)
        
        
        
        # Displays images for peperoni pizza 
        self.pepPizzaIm = Image.open('AdobeStock_223971020.jpeg')
        self.resized = self.pepPizzaIm.resize((100,100))
        self.pepPizzaImNew = ImageTk.PhotoImage(self.resized)
        self.pepPhotoLabel = Label(self, image = self.pepPizzaImNew,bg ='#d9472a')
        self.pepPhotoLabel.place(relx = 0.9,rely = 0.7,anchor = E)



        # Displays images for hawaiian pizza 
        self.hawaiianPizzaIm = Image.open('AdobeStock_89727055.jpeg')
        self.resized = self.hawaiianPizzaIm.resize((100,100))
        self.hawaiianPizzaImNew = ImageTk.PhotoImage(self.resized)
        self.hawaiianPhotoLabel = Label(self, image = self.hawaiianPizzaImNew,bg ='#d9472a')
        self.hawaiianPhotoLabel.place(relx = 0.8,rely = 0.3,anchor = E)
        
        
        
        # Displays images for meatlovers pizza 
        self.mlPizzaIm = Image.open('AdobeStock_144066594.jpeg')
        self.resized = self.mlPizzaIm.resize((100,100))
        self.mlPizzaImNew = ImageTk.PhotoImage(self.resized)
        self.mlPhotoLabel = Label(self, image = self.mlPizzaImNew,bg ='#d9472a')
        self.mlPhotoLabel.place(relx = 0.9,rely = 0.3,anchor = E)
        
        
        
        # These are the labels for the type of pizzas alligned with pictures  
        self.CPPicturelabel = customtkinter.CTkLabel(self,text = 'Cheese Pizza: ')
        self.CPPicturelabel.place(relx = 0.8,rely = 0.85,anchor = E)
        
        self.PPPicturelabel = customtkinter.CTkLabel(self,text = 'Pepperoni Pizza: ')
        self.PPPicturelabel.place(relx = 0.9,rely = 0.85,anchor = E)
        
        self.HPPicturelabel = customtkinter.CTkLabel(self,text = 'Hawaiian Pizza: ')
        self.HPPicturelabel.place(relx = 0.8,rely = 0.45,anchor = E)
        
        self.MPPicturelabel = customtkinter.CTkLabel(self,text = 'Meat-Lovers Pizza: ')
        self.MPPicturelabel.place(relx = 0.9,rely = 0.45,anchor = E)
        
        
        
        
        
        
        
        #entry for Cheese pizzas 
        self.entryCP = customtkinter.CTkEntry(self,bg_color='#d9472a',fg_color='black',border_width=0)
        self.entryCP.place(relx = 0.1,rely = 0.2,anchor = W)

        #entry for Pepperoni pizzas 
        self.entryPP = customtkinter.CTkEntry(self,bg_color='#d9472a',fg_color='black',border_width=0)
        self.entryPP.place(relx = 0.1,rely = 0.3,anchor = W)

        #entry for Hawaiian pizzas 
        self.entryHP = customtkinter.CTkEntry(self,bg_color='#d9472a',fg_color='black',border_width=0)
        self.entryHP.place(relx = 0.1,rely = 0.4,anchor = W)

        #entry for Meat Lovers pizzas 
        self.entryMP = customtkinter.CTkEntry(self,bg_color='#d9472a',fg_color='black',border_width=0)
        self.entryMP.place(relx = 0.1,rely = 0.5,anchor = W)
        
        
        
        
        
        # button that will get order and open window to checkout screen 
        self.checkoutButton = customtkinter.CTkButton(self,text = "Proceed to checkout",command = self.getValues,
                                                      bg_color= '#d9472a',hover_color='gray',corner_radius=10,fg_color='black')
        self.checkoutButton.place(relx = 0.1,rely = 0.8,anchor = SW)
        
        
        # These are the labels for the type of pizzas alligned with entry boxes 
        self.CPlabel = customtkinter.CTkLabel(self,text = 'Cheese Pizza: ')
        self.CPlabel.place(relx = 0.015,rely = 0.2,anchor = W)
        
        self.PPlabel = customtkinter.CTkLabel(self,text = 'Pepperoni Pizza: ')
        self.PPlabel.place(relx = 0.015,rely = 0.3,anchor = W)
        
        self.HPlabel = customtkinter.CTkLabel(self,text = 'Hawaiian Pizza: ')
        self.HPlabel.place(relx = 0.015,rely = 0.4,anchor = W)
        
        self.MPlabel = customtkinter.CTkLabel(self,text = 'Meat Lovers Pizza: ')
        self.MPlabel.place(relx = 0.015,rely = 0.5,anchor = W)
        




        # This is the menu that shows the items and prices 
        self.menuFrame = Frame(self,bg = '#F3B552',padx = 70,pady = 70,)
        self.menuFrame.place(relx = 0.5,rely = 0.5,anchor = CENTER)
        
        
        self.menuLabel = Label(self.menuFrame,font = ('arial',23,),text = 'MENU',bg = '#F3B552')
        self.menuLabel.pack()
        
        self.chLabel = Label(self.menuFrame,text = 'Cheese Pizza: $15',bg = '#F3B552')
        self.chLabel.pack()
        
        self.ppLabel = Label(self.menuFrame,text = 'Pepperoni: $17',bg = '#F3B552')
        self.ppLabel.pack()
        
        self.hpLabel = Label(self.menuFrame,text = 'Hawaiian Pizza: $16',bg = '#F3B552')
        self.hpLabel.pack()
        
        self.mpLabel = Label(self.menuFrame,text = 'Meat-Lovers Pizza: $19',bg = '#F3B552')
        self.mpLabel.pack()







    def getValues(self):

        cusID = getCusID()
        print ('Customer ID:' +str(cusID))

        global total
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
        #cheesePizza(numCheesePizza)
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
        #pepperonniPizza(numPepperoniPizza)
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
        #hawaiianPizza(numHawaiianPizza)
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
        #meatLoversPizza(numMeatLoversPizza)
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
        
        global numCP,numPP,numHP,numMP,total
        
        cusID = getCusID()    #gets the id and row for customer 
        print(cusID)
       
       
       
        self.geometry('1440x500')
        self.title('Checkout')
        self.config(bg = '#d9472a')
        

            
        numCP = sheet['D'+str(cusID)].value   
        numPP = sheet['E'+str(cusID)].value  
        numHP = sheet['F'+str(cusID)].value  
        numMP = sheet['G'+str(cusID)].value
        print(numCP,numPP,numHP,numMP)  
        
        
        
        
        
        # This is the frame and everything that goes inside 
        self.orderFrame = Frame(self,bg = '#F3B552',padx = 70,pady = 70,)
        self.orderFrame.place(relx = 0.1,rely =0.4,anchor = W)
        
        self.heading = Label(self.orderFrame,text = "Order",bg = '#F3B552',font = 'ar 20 bold')
        self.heading.pack()
        #.place(relx = 0.1,rely =0.07,anchor = W)

        # label with pizza order and another label with number of pizzas 
        self.label1 = Label(self.orderFrame,text = 'Cheese Pizzas: ',bg = '#F3B552')             
        self.label1.pack()
        #place(relx = 0.1,rely =0.2,anchor = W)
        self.label1Num = Label(self.orderFrame,text = str(numCP),bg = '#F3B552')    
        self.label1Num.pack()
        #place(relx = 0.1,rely =0.25,anchor = W)
        
        self.label2 = Label(self.orderFrame,text = "Pepperoni Pizzas: ",bg = '#F3B552')   
        self.label2.pack()
        #place(relx = 0.1,rely =0.3,anchor = W)
        self.label2Num = Label(self.orderFrame,text = str(numPP),bg = '#F3B552')    
        self.label2Num.pack()
        #place(relx = 0.1,rely =0.35,anchor = W)
       
        self.label3 = Label(self.orderFrame,text = "Hawaiian Pizzas: ",bg = '#F3B552')    
        self.label3.pack()
        #place(relx = 0.1,rely =0.4,anchor = W)
        self.label3Num = Label(self.orderFrame,text = str(numHP),bg = '#F3B552')    
        self.label3Num.pack()
        #place(relx = 0.1,rely =0.45,anchor = W)
       
        self.label4 = Label(self.orderFrame,text = "Meat Lovers Pizzas: ",bg = '#F3B552')    
        self.label4.pack()
        #place(relx = 0.1,rely =0.5,anchor = W)
        self.label4Num = Label(self.orderFrame,text = str(numMP),bg = '#F3B552')    
        self.label4Num.pack()
        #place(relx = 0.1,rely =0.55,anchor = W)
        
        
        
        
        
        # Displays the total to customer
        self.totalLabel = customtkinter.CTkLabel(self,text = 'Total: $'+str(total),bg_color = '#d9472a',font = ('arial',20))
        self.totalLabel.place(relx = 0.4,rely =0.6,anchor = W)
        
        # Displys the customers order number 
        self.orderNum = customtkinter.CTkLabel(self,text = 'Order: # '+str(cusID),bg_color = '#d9472a',font = ('arial',20))
        self.orderNum.place(relx = 0.4,rely =0.65,anchor = W)
        
        
        # Button to end the transaction and go back to the order screen
        self.checkoutButton = customtkinter.CTkButton(self,text = 'Complete Order',command = self.orderComplete ,bg_color = '#d9472a'
                                                      ,fg_color='black')
        self.checkoutButton.place(relx = 0.8,rely =0.95,anchor = W)
        
        
        # Button to go back to the order screen and change order 
        self.backButton = customtkinter.CTkButton(self,text = 'Back',command = self.back,bg_color = '#d9472a',fg_color='black')
        self.backButton.place(relx = 0.05,rely =0.95,anchor = W)
        
        
        
        
        ## This is the menu that shows the items and prices 
        #self.menuFrame = Frame(self,bg = '#F3B552',padx = 40,pady = 40)
        #self.menuFrame.pack(padx = 50,pady= 0.3)
        #
        #
        #self.menuLabel = Label(self.menuFrame,font = ('arial',23,),text = 'MENU',bg = '#F3B552')
        #self.menuLabel.pack()
        #
        #self.chLabel = Label(self.menuFrame,text = 'Cheese Pizza: $15',bg = '#F3B552')
        #self.chLabel.pack()
        #
        #self.ppLabel = Label(self.menuFrame,text = 'Pepperoni: $17',bg = '#F3B552')
        #self.ppLabel.pack()
        #
        #self.hpLabel = Label(self.menuFrame,text = 'Hawaiian Pizza: $16',bg = '#F3B552')
        #self.hpLabel.pack()
        #
        #self.mpLabel = Label(self.menuFrame,text = 'Meat-Lovers Pizza: $19',bg = '#F3B552')
        #self.mpLabel.pack()
        

    def orderComplete(self):
        print('Order Submitted')
        
        global numCP,numPP,numHP,numMP
        
        cusID = getCusID()               
        newCusID = updateCusID(cusID)

        sheet['A'+str(newCusID)].value = newCusID   # sets the order ID for next customer transaction and saves to excel
        book.save('customerTransactions.xlsx')
        
        # change values to int to pass into the updateinventory
        numCP = int(numCP)
        numPP = int(numPP)
        numHP = int(numHP)
        numMP = int(numMP)
        
        
        #Update Inventory calls 
        cheesePizza(numCP)
        pepperonniPizza(numPP)
        hawaiianPizza(numHP)
        meatLoversPizza(numMP)

    
        #self.destroy()
        self.forget(self)
    
    def back(self):
        # this button will allow customer to go back to change order, need to implement the update inventory to allow changed to 
        # be made before giving this button functionality
        Order(self)
        self.forget(self)
        
        










