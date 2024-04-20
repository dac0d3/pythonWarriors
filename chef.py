# chef views, cooks, then completes order 
# order is sent to runner 


from tkinter import *
import openpyxl
from openpyxl import Workbook, load_workbook
from managerSignIn import *

book = load_workbook('customerTransactions.xlsx')           # excel sheet for transactions
sheet = book.active

class Chef(Toplevel):
    
    def __init__(self, parent):
        super().__init__(parent)
        
        self.title('Orders')
        self.geometry('1400x500')

        # list for pizza data
        self.pizza_data = []

        # fetching data from getOrder def
        self.getOrders()

        for idx, row_data in enumerate(self.pizza_data, start=2):
            Button(self, text=f"Order {idx}", command=lambda i=idx: self.display_row(i)).pack()

        # Creates button for each order
        self.selected_row_label = Label(self, text="")
        self.selected_row_label.pack()

    def getOrders(self):
        for row in range(2, sheet.max_row + 1):
            CP = sheet['D' + str(row)].value
            PP = sheet['E' + str(row)].value
            HP = sheet['F' + str(row)].value
            MLP =sheet['G' + str(row)].value

            if CP is not None:  # if no data is available, then file has reached final order
                self.pizza_data.append(f"Cheese Pizza(s): {CP}, Pepporoni Pizza(s): {PP}, Hawaiian Pizza(s): {HP}, Meat Lovers Pizza(s): {MLP}")
    
    def display_row(self, row_num):
        self.selected_row_label.config(text=f"Order # {row_num}: {self.pizza_data[row_num-2]}")
















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