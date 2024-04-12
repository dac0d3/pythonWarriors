# calculates tax from total and sends to receipt file
# adds total + tax to revenue after order is confirmed 
import math

import openpyxl
from openpyxl import Workbook, load_workbook

book = load_workbook('customerTransactions.xlsx')           # excel sheet for transactions
sheet = book.active


def calculateTax (price):                  
    total = price + (price * .0725)             # calculates tax 
    math.trunc(total)                           # truncates decimals past 100s
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

