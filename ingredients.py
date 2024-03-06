
import openpyxl
from openpyxl import Workbook, load_workbook

book = load_workbook('pythonParlorInventory.xlsx')          # excel sheet
sheet = book.active

def cheesePizza(x):
    dough = sheet['D2'].value
    dough = int(dough) - x
    sheet['D2'].value = dough
    
    cheese = sheet['B2'].value
    cheese = int(cheese) - x
    sheet['B2'].value = cheese
    
    sauce = sheet['C2'].value
    sauce = int(sauce) - x
    sheet['C2'].value = sauce
    
    book.save('pythonParlorInventory.xlsx')
    
    return True 
    

    
    
    



    
    