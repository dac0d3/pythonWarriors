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
        self.config(bg = '#d9472a')
        self.logo = Image.open('pythonLogo.png')
        self.resized = self.logo.resize((200,300))
        self.logoNew = ImageTk.PhotoImage(self.resized)
        
        self.photoLabel = Label(self, image = self.logoNew,bg ='#d9472a')
        self.photoLabel.place(relx = 1,rely = 1,anchor = SE)

        self.order_labels = []  # List to store order labels

        # list for pizza data
        self.pizza_data = []

        # fetching data from getOrder def
        self.getOrders()

      

        for idx, row_data in enumerate(self.pizza_data, start=2):
            btn = Button(self, text=f"Order {idx}", command=lambda i=idx: self.display_row(i),bg='#d9472a',fg='black', highlightbackground='#d9472a',
            highlightcolor='#d9472a')
            btn.pack()
            self.order_labels.append(btn)

        # Selected row label
        self.selected_row_label = Label(self, text="", bg='#d9472a')
        self.selected_row_label.pack()


       

    def getOrders(self):
        for row in range(2, sheet.max_row + 1):
            CP = sheet['D' + str(row)].value
            PP = sheet['E' + str(row)].value
            HP = sheet['F' + str(row)].value
            MLP =sheet['G' + str(row)].value

            if CP is not None:  # if no data is available, then file has reached final order
                self.pizza_data.append(f"Cheese Pizza(s):{CP} | Pepporoni Pizza(s):{PP} | Hawaiian Pizza(s):{HP} | Meat Lovers Pizza(s):{MLP}")
    
    def display_row(self, row_num):
        current_text = self.selected_row_label.cget("text")  
        new_text = f"ORDER#{row_num}: {self.pizza_data[row_num-2]}"  

        if current_text == new_text: 
            self.selected_row_label.config(text="", bg='#FFC902', fg='black')
        else: 
            self.selected_row_label.config(text=new_text, bg='#FFC902', fg='black')

















