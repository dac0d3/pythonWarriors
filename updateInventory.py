
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
    
    return True 


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
    
    return True 


    

    
    
    



    
    