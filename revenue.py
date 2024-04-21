
'''

Module Name: revenue
Documentation Date: 04/21/24
Prog. Name: Diego Carbajal

Module Description: 

Important Functions: 

'''







# calculates tax from total and sends to receipt file
# adds total + tax to revenue after order is confirmed 



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

