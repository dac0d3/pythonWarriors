# calculates tax from total and sends to receipt file
# adds total + tax to revenue after order is confirmed 
import math


revenue = []


def calculateTax (price):                  
    total = price + (price * .0725)             # calculates tax 
    math.trunc(total)                           # truncates decimals past 100s
    return total


# adds total for order in list 
def addToRevenue(total):
    revenue.append(total)
    
    
# calculates total revenue
def getRevenue():
    
    revTotal = 0
    
    for i in len(revenue):
        total = total + revenue[i]

    return revTotal