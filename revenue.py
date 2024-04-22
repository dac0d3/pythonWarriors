
'''

Module Name: revenue
Documentation Date: 04/21/24
Prog. Name: Diego Carbajal

Module Description: This is a utility module that holds the functions for calculating the tax of a total order and the 
revenue for the restaurant from excel. 

Important Functions: 

'calculateTax' : This functions receives one argument which would be the calculated total price of an order and return 
the new total with tax includd.(tax % is .0725)

'getRevenue' : This method is automatically called when the manager signs in to their home page. This function gets the 
total values for every order saved in excel and adds them all up and returns it as the revenue. 

'''



import math

import openpyxl
from openpyxl import Workbook, load_workbook

# excel sheet for transactions
book = load_workbook('customerTransactions.xlsx')           
sheet = book.active


# calculates tax 
# truncates decimals past 100s
def calculateTax (price):                  
    total = price + (price * .0725)             
    math.trunc(total)                           
    return total




# calculates total revenue
def getRevenue():
    
    revenue = 0.0
    num = 2
    total = sheet['H'+str(num)].value
    
    while total is not None:
        total = sheet['H'+str(num)].value
        if total is not None:   
            total = float(total)
            revenue = total + revenue
        num += 1
    
    return revenue

