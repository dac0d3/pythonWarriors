# calculates tax from total and sends to receipt file
# adds total + tax to revenue after order is confirmed 
import math


def calculateTax (price):                  
    total = price + (price * .0725)             # calculates tax 
    math.trunc(total)                           # truncates decimals past 100s
    return total

def addToRevenue(total):
    pass
