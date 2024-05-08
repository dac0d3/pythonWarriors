
import openpyxl
from openpyxl import Workbook, load_workbook

from tkinter import *
import customtkinter
from PIL import ImageTk,Image
import ttkbootstrap as tb
from tkinter import messagebox
from time import *

from email.message import EmailMessage
import ssl 
import smtplib

from revenue import *
from updateInventory import *
from updateTransaction import *
from emailConfirm import *





menu = ['CHEESE PIZZA','PEPPERONI PIZZA','HAWAIIAN PIZZA','MEAT LOVERS PIZZA']
menu_prices = {'CHEESE PIZZA':15,'PEPPERONI PIZZA':17,'HAWAIIAN PIZZA':16,'MEAT LOVERS PIZZA':19} 


numCheesePizza = IntVar
numPepperoniPizza = IntVar
numHawaiianPizza = IntVar
numMeatLoversPizza = IntVar


'''

Class Name: Order
Documentation Date: 04/21/24
Prog. Name: Diego Carbajal

Class Descripion:

Important Functions: 

'__init__' : This function is what creates the window and holds all the buttons and widgets dislayed in the GUI. 

'getValues' : This function gets the values for the pizzas inputed by the customer and calculates the total for the order. 
It finds the total from the dictionary and then send that number to the 'calculateTax' function in the 'revenue' file
to get the new total with tax included. There are preventive if statements to make sure there is an order and will show 
and error message if the customer tries to place an order that has no pizzas in it. And if the order is a valid one, then 
the 'Checkout2' class gets calls closing the current window and openign the new one. 
 
'''

class Order(Toplevel):

    orderPass = 0
    
    
    def __init__(self,parent):
        super().__init__(parent)
                
        
        self.book = load_workbook('customerTransactions.xlsx')
        self.sheet = self.book.active
        
        #self.attributes('-fullscreen',True)
        self.geometry('1100x600')
        self.title('Order Screen')
        self.config(bg = '#bf3c22') 
        
        
        
        
        # This is the menu that shows the items and prices 
        self.menuFrame = Frame(self,bg = '#5EB6D7',padx = 70,pady = 70,highlightbackground="#31120c", highlightcolor="#31120c", highlightthickness=3,bd = 0)
        self.menuFrame.place(relx = 0.9,rely = 0.5,anchor = E)
        
        
        self.menuLabel = customtkinter.CTkLabel(self.menuFrame,font = ('arial',23,),text = 'MENU',bg_color = '#5EB6D7',text_color='black')
        self.menuLabel.grid(row = 1,column = 0,columnspan=2,pady = 2)
        
        self.lineLabel = customtkinter.CTkLabel(self.menuFrame,text = '-----------------------------------------',bg_color = '#5EB6D7',text_color='black')
        self.lineLabel.grid(row = 2,column = 0,columnspan=2,pady = 5) 
        
        # Displays images for Cheese pizza 
        self.cheesePizzaIm = Image.open('360_F_26257008_Amvaw8kdz8KViXR1Gc3fNgl2sfubDV8E.webp')
        self.resized = self.cheesePizzaIm.resize((100,100))
        self.cheesePizzaImNew = ImageTk.PhotoImage(self.resized)
        self.cheesePhotoLabel = Label(self.menuFrame,image = self.cheesePizzaImNew,bg ='#5EB6D7')
        #self.cheesePhotoLabel.place(relx = 0.8,rely = 0.7,anchor = E)  
        self.cheesePhotoLabel.grid(row = 4,column = 0)      
        
        # Displays images for peperoni pizza 
        self.pepPizzaIm = Image.open('AdobeStock_223971020.jpeg')
        self.resized = self.pepPizzaIm.resize((100,100))
        self.pepPizzaImNew = ImageTk.PhotoImage(self.resized)
        self.pepPhotoLabel = Label(self.menuFrame, image = self.pepPizzaImNew,bg ='#5EB6D7')
        #self.pepPhotoLabel.place(relx = 0.9,rely = 0.7,anchor = E)
        self.pepPhotoLabel.grid(row = 4,column = 1)    

        # Displays images for hawaiian pizza 
        self.hawaiianPizzaIm = Image.open('bb501a54-7d1c-4ebd-8b70-0d45e75e66ac.jpg')
        self.resized = self.hawaiianPizzaIm.resize((100,100))
        self.hawaiianPizzaImNew = ImageTk.PhotoImage(self.resized)
        self.hawaiianPhotoLabel = Label(self.menuFrame, image = self.hawaiianPizzaImNew,bg ='#5EB6D7')
        #self.hawaiianPhotoLabel.place(relx = 0.8,rely = 0.3,anchor = E)
        self.hawaiianPhotoLabel.grid(row = 6,column = 0)    
        
        # Displays images for meatlovers pizza 
        self.mlPizzaIm = Image.open('AdobeStock_144066594.jpeg')
        self.resized = self.mlPizzaIm.resize((100,100))
        self.mlPizzaImNew = ImageTk.PhotoImage(self.resized)
        self.mlPhotoLabel = Label(self.menuFrame, image = self.mlPizzaImNew,bg ='#5EB6D7')
        #self.mlPhotoLabel.place(relx = 0.9,rely = 0.3,anchor = E)
        self.mlPhotoLabel.grid(row = 6,column = 1)    
        
        
        
        # These are the labels for the type of pizzas alligned with pictures  
        self.CPPicturelabel = customtkinter.CTkLabel(self.menuFrame,text = 'Cheese Pizza: $15',text_color='black',bg_color='#5EB6D7')
        #self.CPPicturelabel.place(relx = 0.8,rely = 0.85,anchor = E)
        self.CPPicturelabel.grid(row = 3,column = 0)    
        
        self.PPPicturelabel = customtkinter.CTkLabel(self.menuFrame,text = 'Pepperoni Pizza: $17',text_color='black',bg_color='#5EB6D7')
        #self.PPPicturelabel.place(relx = 0.9,rely = 0.85,anchor = E)
        self.PPPicturelabel.grid(row = 3,column = 1)    
        
        self.HPPicturelabel = customtkinter.CTkLabel(self.menuFrame,text = 'Hawaiian Pizza: $16',text_color='black',bg_color='#5EB6D7')
        #self.HPPicturelabel.place(relx = 0.8,rely = 0.45,anchor = E)
        self.HPPicturelabel.grid(row = 5,column = 0)    
        
        self.MPPicturelabel = customtkinter.CTkLabel(self.menuFrame,text = 'Meat-Lovers: $19',text_color='black',bg_color='#5EB6D7')
        #self.MPPicturelabel.place(relx = 0.9,rely = 0.45,anchor = E)
        self.MPPicturelabel.grid(row = 5,column = 1)    
        
        
        
        
        
        
        
        
        
        # Frame for pizza label and their entry boxes
        self.orderFrame = Frame(self,bg = '#FFE6D8',pady = 70, padx = 70,highlightbackground="#31120c", highlightcolor="#31120c", highlightthickness=3,bd = 0)
        self.orderFrame.place(relx = 0.05,rely = 0.5,anchor = W)
        

        # heading for orderFrame
        self.orderHeading = customtkinter.CTkLabel(self.orderFrame,text = "Enter your order",font = ('arial',30,'bold'),bg_color = '#FFE6D8',text_color='#31120c')                             
        self.orderHeading.grid(row = 0,column = 0,columnspan=2)
        
        # Line space
        self.line2 = customtkinter.CTkLabel(self.orderFrame,text = "---------------------------------------------------------",bg_color = '#FFE6D8',text_color='#31120c')                             
        self.line2.grid(row = 1,column = 0,columnspan=2)
        
        #entry for Cheese pizzas 
        self.entryCP = customtkinter.CTkEntry(self.orderFrame,bg_color='#FFE6D8',fg_color='#db7c6b',border_width=0)
        #self.entryCP.place(relx = 0.1,rely = 0.2,anchor = W)
        self.entryCP.grid(row = 2,column = 1,pady = 2)

        #entry for Pepperoni pizzas 
        self.entryPP = customtkinter.CTkEntry(self.orderFrame,bg_color='#FFE6D8',fg_color='#db7c6b',border_width=0)
        #self.entryPP.place(relx = 0.1,rely = 0.3,anchor = W)
        self.entryPP.grid(row = 3,column = 1,pady = 2)

        #entry for Hawaiian pizzas 
        self.entryHP = customtkinter.CTkEntry(self.orderFrame,bg_color='#FFE6D8',fg_color='#db7c6b',border_width=0)
        #self.entryHP.place(relx = 0.1,rely = 0.4,anchor = W)
        self.entryHP.grid(row = 4,column = 1,pady = 2)

        #entry for Meat Lovers pizzas 
        self.entryMP = customtkinter.CTkEntry(self.orderFrame,bg_color='#FFE6D8',fg_color='#db7c6b',border_width=0)
        #self.entryMP.place(relx = 0.1,rely = 0.5,anchor = W)
        self.entryMP.grid(row = 5,column = 1,pady = 2)
        

        
        # These are the labels for the type of pizzas alligned with entry boxes 
        self.CPlabel = customtkinter.CTkLabel(self.orderFrame,text = 'Cheese Pizza: ',text_color='#31120c')
        #self.CPlabel.place(relx = 0.015,rely = 0.2,anchor = W)
        self.CPlabel.grid(row = 2,column = 0,pady = 2)
        
        self.PPlabel = customtkinter.CTkLabel(self.orderFrame,text = 'Pepperoni Pizza: ',text_color='#31120c')
        #self.PPlabel.place(relx = 0.015,rely = 0.3,anchor = W)
        self.PPlabel.grid(row = 3,column = 0,pady = 2)
        
        self.HPlabel = customtkinter.CTkLabel(self.orderFrame,text = 'Hawaiian Pizza: ',text_color='#31120c')
        #self.HPlabel.place(relx = 0.015,rely = 0.4,anchor = W)
        self.HPlabel.grid(row = 4,column = 0,pady = 2)
        
        self.MPlabel = customtkinter.CTkLabel(self.orderFrame,text = 'Meat-Lovers Pizza: ',text_color='#31120c')
        #self.MPlabel.place(relx = 0.015,rely = 0.5,anchor = W)
        self.MPlabel.grid(row = 5,column = 0,pady = 2)
        
 
 
        # button that will get order and open window to checkout screen 
        self.checkoutButton = customtkinter.CTkButton(self.orderFrame,text = "Proceed to checkout",command = self.getValues,
                                                      bg_color= '#FFE6D8',hover_color='gray',corner_radius=10,fg_color='#31120c')
        self.checkoutButton.grid(row = 6,column = 0,columnspan = 2,pady = 30)
        #self.checkoutButton.place(relx = 0.1,rely = 0.8,anchor = SW)





        '''
        # This is the menu that shows the items and prices 
        self.menuFrame = Frame(self,bg = '#FF7D33',padx = 70,pady = 70)
        self.menuFrame.place(relx = 0.5,rely = 0.5,anchor = CENTER)
        
        
        
        
        
        self.menuLabel = Label(self.menuFrame,font = ('arial',23,),text = 'MENU',bg = '#0000FF')
        self.menuLabel.grid(row = 1,column = 0,columnspan=2,pady = 2)
        
        self.lineLabel = Label(self.menuFrame,text = '-------------------------------------',bg = '#0000FF')
        self.lineLabel.grid(row = 2,column = 0,columnspan=2,pady = 5) 
        
        self.chLabel = Label(self.menuFrame,text = 'Cheese Pizza: $15',bg = '#0000FF')
        self.chLabel.grid(row = 3,column = 0,pady = 2,columnspan= 2)
        
        self.ppLabel = Label(self.menuFrame,text = 'Pepperoni: $17',bg = '#0000FF')
        self.ppLabel.grid(row = 4,column = 0,pady = 2,columnspan= 2)
        
        self.hpLabel = Label(self.menuFrame,text = 'Hawaiian Pizza: $16',bg = '#0000FF')
        self.hpLabel.grid(row = 5,column = 0,pady = 2,columnspan= 2)
        
        self.mpLabel = Label(self.menuFrame,text = 'Meat-Lovers Pizza: $19',bg = '#0000FF')
        self.mpLabel.grid(row = 6,column = 0,pady = 2,columnspan= 2)
        '''






    def getValues(self):

        cusID = getCusID()
        print ('Customer ID:' +str(cusID))

        global total
        total = 0
        order = []

        numCheesePizza = self.entryCP.get()
        numPepperoniPizza = self.entryPP.get()
        numHawaiianPizza = self.entryHP.get()
        numMeatLoversPizza = self.entryMP.get()  
        
        

        #Update number of cheese pizzas
        if len(numCheesePizza)== 0:
            numCheesePizza = 0
            numCheesePizza = float(numCheesePizza)
        
        elif numCheesePizza.isdigit():
            numCheesePizza = float(numCheesePizza)
        
        else: 
            messagebox.showwarning('Error',"Enter a valid number!")
            
        #Finds price of pizza in menu
        price1 = menu_prices['CHEESE PIZZA']                             
        #calculates tax
        priceWithTax1 = calculateTax(price1)                              
        priceWithTax1 = priceWithTax1 * numCheesePizza
        order.append(priceWithTax1)
        



        #Update number of cheese pizzas
        if len(numPepperoniPizza)==0:
            numPepperoniPizza = 0
            numPepperoniPizza = float(numPepperoniPizza)
        
        elif numPepperoniPizza.isdigit():
            numPepperoniPizza = float(numPepperoniPizza)
        
        else: 
            messagebox.showwarning('Error',"Enter a valid number!")
            
        #Finds price of pizza in menu
        price2 = menu_prices['PEPPERONI PIZZA']                           
        #calculates tax 
        priceWithTax2 = calculateTax(price2)                              
        priceWithTax2 = numPepperoniPizza * priceWithTax2
        order.append(priceWithTax2)





        #update number of Hawaiian pizzas
        if len(numHawaiianPizza)==0:
            numHawaiianPizza = 0
            numHawaiianPizza = float(numHawaiianPizza)
        
        elif numHawaiianPizza.isdigit():
            numHawaiianPizza = float(numHawaiianPizza)
        
        else: 
            messagebox.showwarning('Error',"Enter a valid number!")
            
        #Finds price of pizza in menu
        price3 = menu_prices['HAWAIIAN PIZZA']   
        #calculates tax                          
        priceWithTax3 = calculateTax(price3)                                
        priceWithTax3 = priceWithTax3 * numHawaiianPizza
        order.append(priceWithTax3)




        #update nuumber of meat lovers pizzas                            
        if len(numMeatLoversPizza)==0:
            numMeatLoversPizza = 0
            numMeatLoversPizza = float(numMeatLoversPizza)
        
        elif numMeatLoversPizza.isdigit():
            numMeatLoversPizza = float(numMeatLoversPizza)
        
        else: 
            messagebox.showwarning('Error',"Enter a valid number!")
            
        #Finds price of pizza in menu
        price4 = menu_prices['MEAT LOVERS PIZZA']   
        #calculates tax                         
        priceWithTax4 = calculateTax(price4)                                 
        priceWithTax4 = priceWithTax4 * numMeatLoversPizza
        order.append(priceWithTax4)



        
        for index in order:
            if total == 0:
                total = index
            else:
                total = total + index
        
        #Round total to 2 decimals 
        total = round(total,2)  
        saveOrder(cusID,numCheesePizza,numPepperoniPizza,numHawaiianPizza,numMeatLoversPizza,total)
        
        print(total)
        print(order)
        
        totalNumPizza = numCheesePizza+numHawaiianPizza+numMeatLoversPizza+numPepperoniPizza
        if total == 0:
            messagebox.showwarning('Error',"You entered no pizzas!")
        elif totalNumPizza > 20:
            messagebox.showwarning('Error',"Number of pizzas may not exceed 20")
        else:
            Checkout2(self)
            self.forget(self)
        





        
'''

Class Name: Checkout2
Documentation Date: 04/21/24
Prog. Name: Diego Carbajal

Class Descripion:

Important Functions: 

'__init__' : This function creates the window and holds all the buttons and widgets dislayed in the GUI. This is 
where the number of pizzas entered in the previous class will be retrieved and be used to show the customer their order. 

'orderComplete' : This function simply saves all the customers pizzas in excel. If the customer doesn't follow through 
with their order and complete the checkout, then this function will never get called making sure only the pizzas that
are payed for are taken account of in the inventory sheet. These values are saved by calling functions from 
the 'updateInventory' file. Further details on how the inventory is saved and tracked can be found in the 
'updateInventory' file. 

'back' : This function simply allows the customer to close the checkout screen and go back to the previous page,
and change their order before checking out. 

'''
    
class Checkout2(Toplevel):
    
    
    def __init__(self,parent):
        super().__init__(parent)
        
        global numCP,numPP,numHP,numMP,total
        

        cusID = getCusID()    #gets the id and row for customer 
        print(cusID)
                       
        #cusName = sheet['B'+str(cusID)].value
        #cusEmail = sheet['C'+str(cusID)].value
        
        numCP = sheet['D'+str(cusID)].value   
        numPP = sheet['E'+str(cusID)].value  
        numHP = sheet['F'+str(cusID)].value  
        numMP = sheet['G'+str(cusID)].value
        print(numCP,numPP,numHP,numMP)  
        
        
        numCP = int(numCP)
        numPP = int(numPP)
        numHP = int(numHP)
        numMP = int(numMP)
        
        # Calculates price of items to display in checkout label
        price = numCP *15
        price2 = numPP *17
        price3 = numHP *16
        price4 = numMP *19
        
        # Gets total of order without tax, finds tax too 
        totalNoTax = price+price2+price3+price4
        tax = total-totalNoTax
        tax = round(tax,2)
        
        print('total with tax :'+str(total))
        print('total no tax: '+str(totalNoTax))
        print('tax: '+str(tax))
        
        self.geometry('1100x600')
        self.title('Checkout')
        self.config(bg = '#d9472a')
        
        
        
        
        
        
        
        
        
        # This is the frame and everything to go inside 
        self.orderFrame = Frame(self,bg = '#FFE6D8',padx = 55,pady = 100,highlightbackground="#31120c", highlightcolor="#31120c", highlightthickness=3,bd = 0)
        self.orderFrame.place(relx = 0.5,rely =0.5,anchor = CENTER)
        
        
        # Label for customer ID 
        self.heading = Label(self.orderFrame,text = "Order :   "+str(cusID),bg = '#FFE6D8',font = 'ar 20 bold',fg = 'black')
        self.heading.grid(row = 1,column=0,columnspan=3)

        # Space between labels
        self.space = customtkinter.CTkLabel(self.orderFrame,text = ' ',bg_color = '#FFE6D8',)
        self.space.grid(row = 2,column=0,pady = 8)
        
        # Label to display date
        date_string = strftime("%B %d, %Y")
        self.date = Label(self.orderFrame,text = date_string,font = ('arial',14),fg = 'black',bg = '#FFE6D8')
        self.date.grid(row = 3,column=0)

        
        # Label to display time
        time_string = strftime('%I:%M %p')
        self.time = Label(self.orderFrame,text = time_string,font= ('arial',14),fg = 'black',bg = '#FFE6D8')
        self.time.grid(row = 3,column=2)



        self.topLine = Label(self.orderFrame,
                             text = '---------------------------------------------------------',
                             bg = '#FFE6D8',fg='black')
        self.topLine.grid(row = 4,column = 0,columnspan=3,pady = 4)
        
        
        

        self.qtyLabel = Label(self.orderFrame,text = 'Qty',bg = '#FFE6D8',fg = 'black')
        self.qtyLabel.grid(row = 5, column = 0,pady = 2)
        
        self.itemLabel = Label(self.orderFrame,text = 'Item',bg = '#FFE6D8',fg = 'black')
        self.itemLabel.grid(row = 5, column = 1,pady = 2)
        
        self.priceLabel = Label(self.orderFrame,text = 'Price',bg = '#FFE6D8',fg = 'black')
        self.priceLabel.grid(row = 5, column = 2,pady = 2)
        
        
        
        # If the value for that pizza is >=1 then it will show on the order frame 
        if numCP != 0:
            self.label1 = Label(self.orderFrame,text = 'Cheese Pizza',bg = '#FFE6D8',font = ('arial',14),fg = 'black')             
            self.label1.grid(row = 6,column=1)
            
            self.label1Num = Label(self.orderFrame,text = str(numCP),bg = '#FFE6D8',font = ('arial',14),fg = 'black')    
            self.label1Num.grid(row = 6,column=0)
            
            self.priceLabel1 = Label(self.orderFrame,text = '$ '+str(price) ,bg = '#FFE6D8',font = ('arial',14),fg = 'black')
            self.priceLabel1.grid(row = 6,column=2)
        
        
        if numPP != 0:
            self.label2 = Label(self.orderFrame,text = "Pepperoni Pizza",bg = '#FFE6D8',font = ('arial',14),fg = 'black')   
            self.label2.grid(row = 7,column=1)
            
            self.label2Num = Label(self.orderFrame,text = str(numPP),bg = '#FFE6D8',font = ('arial',14),fg = 'black')    
            self.label2Num.grid(row = 7,column=0)
            
            self.priceLabel1 = Label(self.orderFrame,text = '$ '+str(price2) ,bg = '#FFE6D8',font = ('arial',14),fg = 'black')
            self.priceLabel1.grid(row = 7,column=2)


        if numHP != 0:
            self.label3 = Label(self.orderFrame,text = "Hawaiian Pizza",bg = '#FFE6D8',font = ('arial',14),fg = 'black')    
            self.label3.grid(row = 8,column=1)
            
            self.label3Num = Label(self.orderFrame,text = str(numHP),bg = '#FFE6D8',font = ('arial',14),fg = 'black')    
            self.label3Num.grid(row = 8,column=0)
            
            self.priceLabel1 = Label(self.orderFrame,text = '$ '+str(price3) ,bg = '#FFE6D8',font = ('arial',14),fg = 'black')
            self.priceLabel1.grid(row = 8,column=2)


        if numMP != 0:
            self.label4 = Label(self.orderFrame,text = "Meat Lovers Pizza",bg = '#FFE6D8',font = ('arial',14),fg = 'black')    
            self.label4.grid(row = 9,column=1)
            
            self.label4Num = Label(self.orderFrame,text = str(numMP),bg = '#FFE6D8',font = ('arial',14),fg = 'black')    
            self.label4Num.grid(row = 9,column=0)
            
            self.priceLabel1 = Label(self.orderFrame,text = '$ '+str(price4) ,bg = '#FFE6D8',font = ('arial',14),fg = 'black')
            self.priceLabel1.grid(row = 9,column=2)

        

        
        self.bottomLine = Label(self.orderFrame,
                             text = '---------------------------------------------------------',
                             bg = '#FFE6D8',fg='black')
        self.bottomLine.grid(row = 10,column = 0,columnspan=3,pady = 10)  
        
        
        
        # Displays the subtotal to customer
        self.total2Label = customtkinter.CTkLabel(self.orderFrame,text = 'Subtotal: $'+str(totalNoTax),
                                                 bg_color = '#FFE6D8',font = ('arial',14),text_color = 'black')
        self.total2Label.grid(row = 11,column=0)
        
        # Displays the tax to customer
        self.taxLabel = customtkinter.CTkLabel(self.orderFrame,text = 'Tax: $'+str(tax),
                                                 bg_color = '#FFE6D8',font = ('arial',14),text_color = 'black')
        self.taxLabel.grid(row = 12,column=0)
        
        # Displays the total plus tax to customer
        self.totalLabel = customtkinter.CTkLabel(self.orderFrame,text = 'Total: $'+str(total),
                                                 bg_color = '#FFE6D8',font = ('arial',16),text_color = 'black')
        self.totalLabel.grid(row = 13,column=0)

        # Space between labels
        self.space = customtkinter.CTkLabel(self.orderFrame,text = ' ',bg_color = '#FFE6D8',)
        self.space.grid(row = 14,column=0,pady = 15)
        
        # Dislpays the thank you 
        self.thankYouLabel = customtkinter.CTkLabel(self.orderFrame,text = 'Thank you for visiting',bg_color = '#FFE6D8',font = ('arial',17),text_color = 'black')
        self.thankYouLabel.grid(row = 15,column=0,columnspan = 3)
        
        # Displays the restaurant Name
        self.restaurantLabel = customtkinter.CTkLabel(self.orderFrame,text = 'Python Parlor',bg_color = '#FFE6D8',font = ('arial',17),text_color = 'black')
        self.restaurantLabel.grid(row = 16,column=0,columnspan = 3)

        
        
        
        
        
        
        # Button to end the transaction and go back to the order screen
        self.checkoutButton = customtkinter.CTkButton(self,text = 'Submit Order',command = self.orderComplete ,bg_color = '#d9472a'
                                                      ,fg_color='black')
        self.checkoutButton.place(relx = 0.8,rely =0.95,anchor = W)
        
        
        # Button to go back to the order screen and change order 
        self.backButton = customtkinter.CTkButton(self,text = 'Back',command = self.back,bg_color = '#d9472a',fg_color='black')
        self.backButton.place(relx = 0.05,rely =0.95,anchor = W)
        
    

    def orderComplete(self):
        print('Order Submitted')
        
        global numCP,numPP,numHP,numMP
        
        cusID = getCusID()  
        
        # This gets the customer email from excel and calls method to send customer email
        #cusEmail = sheet['C'+str(cusID)].value
        #emailConf(cusEmail)
        
                  
        updateCusID(cusID)
        
        
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
        
        
        self.forget(self)
        from openKiosk import run2
        run2()
        
        #self.forget(self)
       
        # Calling this function stops the current transaction and starts a new one
        
        
        
        
        
        

           
        
    def back(self):
        Order(self)
        self.forget(self)
        
