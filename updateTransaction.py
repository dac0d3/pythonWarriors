import openpyxl
from openpyxl import Workbook, load_workbook
from checkout import Checkout


book = load_workbook('customerTransactions.xlsx')           # excel sheet for inventory
sheet = book.active


def saveValues(cusID,name,email):
        
    name = str(name)
    email = str(email)
    
    sheet['B'+str(cusID)].value = name               # stores name in excel 
    sheet['C'+str(cusID)].value = email              # stores email in excel
        
    book.save('customerTransactions.xlsx')
        
    excelName = sheet['B'+str(cusID)].value               # gets name in excel 
    excelEmail = sheet['C'+str(cusID)].value            # gets email in excel
        
    print(excelName,excelEmail)
    
    
    
def saveOrder(cusID,numCP,numPP,numHP,numMP,total):
    
    numCP = int(numCP)
    numPP = int(numPP)
    numHP = int(numHP)
    numMP = int(numMP)
    
    sheet['D'+str(cusID)].value = numCP
    sheet['E'+str(cusID)].value = numPP
    sheet['F'+str(cusID)].value = numHP
    sheet['G'+str(cusID)].value = numMP
    sheet['H'+str(cusID)].value = total
    
    print(numCP,numPP,numHP,numMP,total)
    
    book.save('customerTransactions.xlsx')
    
    
    
def getCusID():
    cusID = sheet['A2'].value
    print('Customer ID: '+str(cusID))
    cusID = int(cusID)
    
    return cusID
   
    
    
def updateCusID(cusID):
    cusID = cusID +1
    
    return cusID

