import openpyxl
from openpyxl import Workbook, load_workbook



book = load_workbook('customerTransactions.xlsx')           # excel sheet for transactions
sheet = book.active


cus = []

#cusID = sheet['A2'].value
#print('Customer ID: '+str(cusID))
#cusID = int(cusID)

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



# fix whle loop
#def resetTransactions():
#    row = 2
#    value = sheet['A'+str(row)].value
#    
#    
#    while value != 0:
#        
#        sheet['A'+str(row)].value = 0
#        sheet['B'+str(row)].value = 0
#        sheet['C'+str(row)].value = 0
#        sheet['D'+str(row)].value = 0
#        sheet['E'+str(row)].value = 0
#        sheet['F'+str(row)].value = 0
#        sheet['G'+str(row)].value = 0
#        sheet['H'+str(row)].value = 0
#        
#        row = row+1
#        value = sheet['A'+str(row)].value
#        print(1)
#        book.save('customerTransactions.xlsx')
#    
#    print('Transactions Reset!')
        