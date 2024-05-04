
from tkinter import *
import openpyxl
from openpyxl import Workbook, load_workbook
from managerSignIn import *
import customtkinter

from main import Main2


# excel sheet for transactions
book = load_workbook('customerTransactions.xlsx')           
sheet = book.active


'''
Class Name: Chef

Date: 4/21/2024

Programmer's name: Adrian Ramos

Class Description: This class loops through the customer transactions excel sheet and puts all the orders into a list for reference.
The same logic is used to make buttons that associate with a four pizza set. Once clicked a label will be showed with the amount of pizza
for each combination. This class also handles the GUI for the chef window.

Important Functions: 
The getOrders() function is the key to this class. It provides the data that will be used to create the buttons that 
tell the chef what orders to cook. The for loop will place the int values to the CP, PP, HP, and MLP variables which are associated with
a specific type of pizza. 
There is also a for loop in def __init__() that creates button and it's directly associate with the customers order
by matching the index of the orders created in the getOrders() function. The self.order_labels.append(btn) handles this responsibility
The display_row() functions allows the order GUI to disappear and reappear as needed. It also handles the task of displaying the correct order
depending on the button that is choosen. There is an if-else statment that handles this by comparing the text that is associated with the
button. If it matches then the order will disappear on the second click, if it's not, then the new text will display as it is either a 
diifferent order, or identical to the last order meaning no change is needed.

Data Structure(s): Lists

Algorithm: String Matching: The display_row() functon uses this algorithm to detect wether a change needs to be made to the order 
associated with the button or to make the current order disappear if it's no longer needed.

'''


class Chef(Toplevel):
    
    def __init__(self, parent):
        super().__init__(parent)
        
        #GUI for chef window
        self.title('Orders')
        self.geometry('1000x500')
        self.config(bg = '#d9472a')
        

    
        # List to order labels
        self.order_labels = []

        # list for order data
        self.order_data = []

        # fetching data from getOrder def
        self.getOrders()
        
        self.exitButton = customtkinter.CTkButton(self,text = 'Exit',command = self.exitPage)
        self.exitButton.place(relx = 0.8,rely = 0.8,anchor = CENTER)

      

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


    # Method to exit chef home Page
    def exitPage(self):
        Main2(self)
        self.forget(self)

       
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
            self.selected_row_label.config(text="", bg='#FFC902', fg='black',font=('Arial', 18))
        else: 
            self.selected_row_label.config(text=new_text, bg='#FFC902', fg='black',font=('Arial', 18))


