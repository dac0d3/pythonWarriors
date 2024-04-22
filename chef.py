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
        
        #GUI for chef window
        self.title('Orders')
        self.geometry('1400x500')
        self.config(bg = '#d9472a')
        

    
        # List to order labels
        self.order_labels = []

        # list for order data
        self.order_data = []

        # fetching data from getOrder def
        self.getOrders()

      

        for idx, row_data in enumerate(self.order_data, start=2):
            #function call
            btn = Button(self, text=f"Order {idx - 1}", command=lambda i=idx: self.display_row(i),bg='#d9472a',fg='black', highlightbackground='#d9472a',
            highlightcolor='#d9472a')
            btn.pack(side=TOP, anchor=W)
            
            #adds button to list
            self.order_labels.append(btn)

        # Selected row label
        self.selected_row_label = Label(self, text="", bg='#d9472a')
        self.selected_row_label.pack() 


       
    # def for looping through customer transactions to get order data
    def getOrders(self):
        for row in range(2, sheet.max_row + 1):
            CP = sheet['D' + str(row)].value
            PP = sheet['E' + str(row)].value
            HP = sheet['F' + str(row)].value
            MLP =sheet['G' + str(row)].value

            if CP is not None:  # if no data is available, then file has reached final order
                self.order_data.append(f"Cheese Pizza(s){CP}\nPepperoni Pizza(s):{PP}\nHawaiian Pizza(s):{HP}\nMeat Lovers Pizza(s):{MLP}")
    
    def display_row(self, row_num):
        #get widget value
        current_text = self.selected_row_label.cget("text")  
        #adjusting list by 2 b/c excel index starting at 2 and 
        new_text = f"ORDER #{row_num -1}\n{self.order_data[row_num-2]}"  

        if current_text == new_text: 
            self.selected_row_label.config(text="", bg='#FFC902', fg='black',font=('Arial', 20))
        else: 
            self.selected_row_label.config(text=new_text, bg='#FFC902', fg='black',font=('Arial', 20))



















root = Tk()
chef_window = Chef(root)
chef_window.mainloop()
















