
'''

Module Name: updateInventory
Documentation Date: 04/21/24
Prog. Name: Diego Carbajal

Module Description: This is a utility module that holds the functions for anything related to updating, setting, or getting
information regarding the inventory for the restaurant. 

Important Functions: 

'cheesePizza' , 'pepperoniPizza' , 'hawaiianPizza' , and 'meatLoversPizza' : These functions may have different names but
they all do the exact same thing. They receive one argument when called() which is the number of pizzas for that order) and 
then subtract 1 package for every ingredient for every pizza in the order. For example, the cheesePizza function with an
argument of 2 will subtract 2 units of cheese, dough, and tomatoe sauce from the inventory then update and save the new 
inventory value to keep the values up to date.


'restockInventory' : This function is only available to be called by the manager from their homepage. This function
essentially set all the values in the inventory back to 1000 which is the full capacity for the inventory. Basically simulating 
the resupplying of the restaurants inventory. 

'''



import openpyxl
from openpyxl import Workbook, load_workbook

# excel sheet for inventory
book = load_workbook('pythonParlorInventory.xlsx')          
sheet = book.active



# updates inventory with ingredients in a cheese pizza 
def cheesePizza(x):                           
    
    # updates dough
    dough = sheet['D2'].value  
    dough = int(dough) - x
    sheet['D2'].value = dough
    
    # updates cheese
    cheese = sheet['B2'].value  
    cheese = int(cheese) - x
    sheet['B2'].value = cheese
    
    # updates sauce
    sauce = sheet['C2'].value   
    sauce = int(sauce) - x
    sheet['C2'].value = sauce
    
    # saves changes in excel sheet 
    book.save('pythonParlorInventory.xlsx')     
    
    

# updates inventory with ingredients in a pepperonni pizza 
def pepperonniPizza(x):                           
    
    # updates dough
    dough = sheet['D2'].value   
    dough = int(dough) - x
    sheet['D2'].value = dough
    
    # updates cheese
    cheese = sheet['B2'].value  
    cheese = int(cheese) - x
    sheet['B2'].value = cheese
    
    # updates sauce
    sauce = sheet['C2'].value   
    sauce = int(sauce) - x
    sheet['C2'].value = sauce
    
    # updates pepperonni
    pep = sheet['A2'].value         
    pep = int(pep) - x
    sheet['A2'].value = pep
    
    # saves changes in excel sheet 
    book.save('pythonParlorInventory.xlsx')     
    


# updates inventory with ingredients in a hawaiian pizza 
def hawaiianPizza(x):                           
    
    # updates dough
    dough = sheet['D2'].value   
    dough = int(dough) - x
    sheet['D2'].value = dough
    
    # updates cheese
    cheese = sheet['B2'].value  
    cheese = int(cheese) - x
    sheet['B2'].value = cheese
    
    # updates sauce
    sauce = sheet['C2'].value   
    sauce = int(sauce) - x
    sheet['C2'].value = sauce
    
    # updates ham
    ham = sheet['E2'].value         
    ham = int(ham) - x
    sheet['E2'].value = ham
    
    # updates pineapple
    pineapple = sheet['F2'].value         
    pineapple = int(pineapple) - x
    sheet['F2'].value = pineapple
    
    # saves changes in excel sheet 
    book.save('pythonParlorInventory.xlsx')     
    


# updates inventory with ingredients in a meat lovers pizza 
def meatLoversPizza(x):                           
    
    # updates dough
    dough = sheet['D2'].value  
    dough = int(dough) - x
    sheet['D2'].value = dough
    
    # updates cheese
    cheese = sheet['B2'].value  
    cheese = int(cheese) - x
    sheet['B2'].value = cheese
    
    # updates sauce
    sauce = sheet['C2'].value   
    sauce = int(sauce) - x
    sheet['C2'].value = sauce
    
    # updates ham
    ham = sheet['E2'].value         
    ham = int(ham) - x
    sheet['E2'].value = ham
    
    # updates pepperonni
    pep = sheet['A2'].value         
    pep = int(pep) - x
    sheet['A2'].value = pep
    
    # updates sausage
    sausage = sheet['G2'].value         
    sausage = int(pep) - x
    sheet['G2'].value = sausage
    
    # updates bacon
    bacon = sheet['H2'].value         
    bacon = int(bacon) - x
    sheet['H2'].value = bacon
    
    # saves changes in excel sheet 
    book.save('pythonParlorInventory.xlsx')     
    


# resets inventory to it's initial values, will only be available to call from manager home page
def restockInventory():
    sheet['A2'].value = 1000         # pepperonin
    sheet['B2'].value = 1000         # cheese
    sheet['C2'].value = 1000         # sause
    sheet['D2'].value = 1000         # dough
    sheet['E2'].value = 1000         # ham
    sheet['F2'].value = 1000         # pineapple
    sheet['G2'].value = 1000         # sausage
    sheet['H2'].value = 1000         # bacon
    sheet['I2'].value = 1000         # jalapenos
    
    book.save('pythonParlorInventory.xlsx')
    
