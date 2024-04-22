
'''

Module Name: updateTransaction
Documentation Date: 04/21/24
Prog. Name: Diego Carbajal

Module Description: This is a utility module that holds the functions for anything related to updating, setting, or getting
information regarding the customer transactions for the restaurant. 

Important Functions: 

'saveValues' : This functions is called with 3 arguments. The order number (int), name(String), and email(string). It then uses
the order number to store the given name and email into the coresponding row in excel. 

'saveOrder' : This function is called with 5 arguments. These are the order number(int), number of cheese pizza(int),
number of pepperoni pizzas(int),nuumber of hawaiian pizzas(int), number of meat lovers pizzas(int), and total (float). 
Then using the given order number, it saves the values for the order into the correct row on the excel sheet which matches
the row their name and email are on. 

'getCusID' :

'updateCusID' : 

'addOneCust' : 

'resetTransactions' : This function is only available to the manager from their home page. All it does is wipe out the 
current excel sheet essentially making a brand new sheet avilable for another day of customer transactions. It uses a loop
to check if there is an order in that row, and if so, it will set all the values in that row to 'None'. 


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
    
   
   
    
# sets the customers ID by getting the length of the list and adding 1
def getCusID():

    return len(cus)+1

# this method is called to add one to the cusID so that it can be saved for the next customer 
# saves the order ID for next customer transaction in excel
def updateCusID(cusID):
    cusID = cusID +1
    
    
    sheet['A'+str(cusID)].value = cusID   
    book.save('customerTransactions.xlsx')
    
    return cusID

# this method is called every time a new transaction starts to keep track of new customers
def addOneCust():
    cus.append(1)






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

