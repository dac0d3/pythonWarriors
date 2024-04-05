import openpyxl
from openpyxl import Workbook, load_workbook
from tkinter import *

book = load_workbook('customerTransactions.xlsx')
sheet = book.active

class Main:
    
    cusID = sheet['A2'].value
    cusID = int(cusID)
    #print('Customer ID: '+str(cusID))
    
    #window = Tk()
    #window.title('Main')
    #window.geometry('1440x900')




    def main():
        import customer 
        import order 
        import checkout

    main()






    #restockInventory()

    #window.mainloop()