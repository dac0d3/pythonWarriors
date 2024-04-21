
import openpyxl
from openpyxl import Workbook, load_workbook


book = load_workbook('pythonParlorInventory.xlsx')          # excel sheet for inventory
sheet = book.active



# updates inventory with ingredients in a cheese pizza 
def cheesePizza(x):                           
    dough = sheet['D2'].value   # updates dough
    dough = int(dough) - x
    sheet['D2'].value = dough
    
    cheese = sheet['B2'].value  # updates cheese
    cheese = int(cheese) - x
    sheet['B2'].value = cheese
    
    sauce = sheet['C2'].value   # updates sauce
    sauce = int(sauce) - x
    sheet['C2'].value = sauce
    
    book.save('pythonParlorInventory.xlsx')     # saves changes in excel sheet 
    
    

# updates inventory with ingredients in a pepperonni pizza 
def pepperonniPizza(x):                           
    dough = sheet['D2'].value   # updates dough
    dough = int(dough) - x
    sheet['D2'].value = dough
    
    cheese = sheet['B2'].value  # updates cheese
    cheese = int(cheese) - x
    sheet['B2'].value = cheese
    
    sauce = sheet['C2'].value   # updates sauce
    sauce = int(sauce) - x
    sheet['C2'].value = sauce
    
    pep = sheet['A2'].value         # updates pepperonni
    pep = int(pep) - x
    sheet['A2'].value = pep
    
    book.save('pythonParlorInventory.xlsx')     # saves changes in excel sheet 
    


# updates inventory with ingredients in a hawaiian pizza 
def hawaiianPizza(x):                           
    dough = sheet['D2'].value   # updates dough
    dough = int(dough) - x
    sheet['D2'].value = dough
    
    cheese = sheet['B2'].value  # updates cheese
    cheese = int(cheese) - x
    sheet['B2'].value = cheese
    
    sauce = sheet['C2'].value   # updates sauce
    sauce = int(sauce) - x
    sheet['C2'].value = sauce
    
    ham = sheet['E2'].value         # updates ham
    ham = int(ham) - x
    sheet['E2'].value = ham
    
    pineapple = sheet['F2'].value         # updates pineapple
    pineapple = int(pineapple) - x
    sheet['F2'].value = pineapple
    
    book.save('pythonParlorInventory.xlsx')     # saves changes in excel sheet 
    


# updates inventory with ingredients in a meat lovers pizza 
def meatLoversPizza(x):                           
    dough = sheet['D2'].value   # updates dough
    dough = int(dough) - x
    sheet['D2'].value = dough
    
    cheese = sheet['B2'].value  # updates cheese
    cheese = int(cheese) - x
    sheet['B2'].value = cheese
    
    sauce = sheet['C2'].value   # updates sauce
    sauce = int(sauce) - x
    sheet['C2'].value = sauce
    
    ham = sheet['E2'].value         # updates ham
    ham = int(ham) - x
    sheet['E2'].value = ham
    
    pep = sheet['A2'].value         # updates pepperonni
    pep = int(pep) - x
    sheet['A2'].value = pep
    
    sausage = sheet['G2'].value         # updates sausage
    sausage = int(pep) - x
    sheet['G2'].value = sausage
    
    bacon = sheet['H2'].value         # updates bacon
    bacon = int(bacon) - x
    sheet['H2'].value = bacon
    
    book.save('pythonParlorInventory.xlsx')     # saves changes in excel sheet 
    


# resets inventory to it's initial values, will only be available to call in the manager file 
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
    
