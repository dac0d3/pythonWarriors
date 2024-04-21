
'''

Module Name: updateTransaction
Documentation Date: 04/21/24
Prog. Name: Diego Carbajal

Module Description: 

Important Functions: 

'''




import openpyxl
from openpyxl import Workbook, load_workbook


# excel sheet for transactions
book = load_workbook('customerTransactions.xlsx')           
sheet = book.active


cus = []



def saveValues(cusID,name,email):
        
    name = str(name)
    email = str(email)
    # stores name in excel 
    sheet['B'+str(cusID)].value = name  
    # stores email in excel             
    sheet['C'+str(cusID)].value = email              
        
    book.save('customerTransactions.xlsx')
        
    # gets name in excel 
    excelName = sheet['B'+str(cusID)].value  
    # gets email in excel             
    excelEmail = sheet['C'+str(cusID)].value            
        
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
    
    
# finds cus ID by adding up the number of trnsactions in list and adding one
def getCusID():

    return len(cus)+1
   
def updateCusID(cusID):
    cusID = cusID +1
    
    return cusID

def resetCusID():
    cusID = 2
   
def addOneCust():
    cus.append(1)

# each cus ID will be one more than the customer transaction




def resetTransactions():
    row = 2
    value = sheet['A'+str(row)].value
    
    while value != None:
        
        if row ==2:
            sheet['B'+str(row)].value = None
            sheet['C'+str(row)].value = None
            sheet['D'+str(row)].value = None
            sheet['E'+str(row)].value = None
            sheet['F'+str(row)].value = None
            sheet['G'+str(row)].value = None
            sheet['H'+str(row)].value = None
        else:
            sheet['A'+str(row)].value = None
            sheet['B'+str(row)].value = None
            sheet['C'+str(row)].value = None
            sheet['D'+str(row)].value = None
            sheet['E'+str(row)].value = None
            sheet['F'+str(row)].value = None
            sheet['G'+str(row)].value = None
            sheet['H'+str(row)].value = None
        
        row = row+1
        value = sheet['A'+str(row)].value
        book.save('customerTransactions.xlsx')
        
        print(value)
        
    sheet['A'+str(row+1)].value = None
    sheet['A'+str(row+2)].value = None
    book.save('customerTransactions.xlsx')
    
    print('Transactions Reset!')

