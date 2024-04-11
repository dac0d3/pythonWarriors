# chef views, cooks, then completes order 
# order is sent to runner 


from tkinter import *
import openpyxl
from openpyxl import Workbook, load_workbook



class Chef(Toplevel):
    
    def __init__(self,parent):
        super().__init__(parent)
        
        self.title('Chef GUI')
        self.geometry('1400x500')
        
    


















#book = load_workbook('customerTransactions.xlsx')
#sheet = book.active
#
#row = 2
#cusID = row
#
#    
#numCP = sheet['D'+str(row)].value
#numPP = sheet['E'+str(row)].value
#numHP = sheet['F'+str(row)].value
#numMP = sheet['G'+str(row)].value
#
#totalPizzas = numCP + numPP + numHP + numMP
#
#def closeWindow():
#    window.destroy()
#    
#    
#if totalPizzas == 0:
#    
#    window = Tk()
#    window.title('Chef Screen')
#
#    label = Label(window,text = 'No pizzas to cook',bg='white',fg = 'black')
#    label.pack()
#    
#    button = Button(window,text = 'Submit',command = closeWindow)
#    button.pack()
#    
#    window.mainloop()
#
#else:
#    print("Total number of pizzas to cook: "+str(totalPizzas))
#    
#    