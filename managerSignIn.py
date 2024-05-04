
from tkinter import *
from tkinter import messagebox
import customtkinter
from PIL import ImageTk,Image

from updateInventory import *
from updateTransaction import *
from revenue import *

username = 'u'
password = 'p'


'''

Class Name: ManagerSignIn
Documentation Date: 04/21/24
Prog. Name: Diego Carbajal

Class Descripion:
When this class is called, it will promt the actor with a manager sign in window where he/she will
see two entry boxes, one for their username and one for their password. If their credentials are correct, then they will
move from the sign in screen to the home page will is called from the 'ManagerHomePage' class. 

Important Functions: 
There are two functions in this class, 'checkCredentials' and 'goBack'. 'checkCredentials' is the funcion that holds
the logic for the authentication of the managers sign in credentials. It's a simple if statement that verifies that the
username and password entered are correct. If so, the manager will get granted access to their homepage. If incorrect, there
will be an error message box letting the actor know that either their password or username were incorrect. The other
function, 'goBack' , is simply a function that allows the user to go back to the previous screen and close the manager sign
in screen. 

'__init__' : This function is what creates the window and holds all the buttons and widgets dislayed in the GUI. 

'''

class ManagerSignIn(Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        
        self.geometry('1000x500')
        self.title('Manager Sign In')
        self.config(bg = '#d9472a')
        
        self.logo = Image.open('pythonLogo.png')
        self.resized = self.logo.resize((510,400))
        self.logoNew = ImageTk.PhotoImage(self.resized)
        
        self.photoLabel = Label(self, image = self.logoNew,bg ='#d9472a')
        self.photoLabel.place(relx = 0.7,rely = 0.43,anchor = CENTER)
        
        
        
        
        
        #Frame for text and entry boxes
        self.signFrame = Frame(self,pady = 50,padx = 30,bg = 'red')
        self.signFrame.place(relx = 0.05,rely = 0.43,anchor = W)
        
        #Heading 
        self.managerTitle = customtkinter.CTkLabel(self.signFrame ,text = "Manager Sign-In",font = ('arial',26),bg_color = '#d9472a')
        self.managerTitle.grid(row = 0,column = 0,columnspan = 2,pady = 10)
        
        self.space1 = customtkinter.CTkLabel(self.signFrame ,text = '' )
        self.space1.grid(row = 1,column = 0,pady = 10)
        
        #Username label
        self.user = customtkinter.CTkLabel(self.signFrame ,text = 'Enter Username: ',font = ('arial',15))
        self.user.grid(row = 2,column = 0,pady = 2)
        
        # username entry
        self.entry1= customtkinter.CTkEntry(self.signFrame ,bg_color='#d9472a',fg_color='black')
        self.entry1.grid(row = 2,column = 1,pady = 2)
        
        #password label
        self.passw = customtkinter.CTkLabel(self.signFrame ,text = 'Enter Password: ',font = ('arial',15))
        self.passw.grid(row = 3,column = 0,pady = 2)
        
        #password entry
        self.entry2 = customtkinter.CTkEntry(self.signFrame ,bg_color='#d9472a',fg_color='black')
        self.entry2.grid(row = 3,column = 1,pady = 2)
        
        self.space2 = customtkinter.CTkLabel(self.signFrame ,text = '' )
        self.space2.grid(row = 4,column = 0,pady = 5)
        
        #submit button
        self.submit = customtkinter.CTkButton(self.signFrame ,text = "Submit",command = self.checkCredentials,
                                              bg_color='#d9472a',fg_color='black',height = 12,width = 20)
        self.submit.grid(row = 5,column = 0,pady = 2,columnspan = 2)
    
    
    
        # return button
        self.returnButton = customtkinter.CTkButton(self,text = 'Back',command = self.goBack,
                                                    bg_color='#d9472a',fg_color='black',height = 10,width = 10)
        self.returnButton.place(relx = 0.1,rely = 0.9,anchor = SW)
    
    
    def checkCredentials(self):
        usName = self.entry1.get()
        passW = self.entry2.get()
        
        if usName == username and passW == password:
            print('Manager Signed in!')
            ManagerHomePage(self)
            self.forget(self)
            
        else:
            messagebox.showwarning('Error',"Incorrect password or username")
    
    
    def goBack(self):
        self.withdraw()   
        from main import Main2
        Main2(self)
    
    
    
    

'''

Class Name: ManagerHomePage
Documentation Date: 04/21/24
Prog. Name: Diego Carbajal

Class Descripion: When this class is called, the manager is now shown the manager home page. Here the manager can do 
some tasks like reset customer transactions and resupply the inventory. The manager is also shown the total amount of money
the restaurant has made thoughout the day. 

Important Functions: 
'__init__' : This function is what creates the window and holds all the buttons and widgets dislayed in the GUI. 

'resetInventory' : This functions calls another function called 'restockInventory', which is in the updateInventory module 
that resets all the restaurants inventory back to it's full capacaity, essentially resupplying. 
Further explanation on how this function works is explained in the updateInventory file. 

'resetTrans' : This functions calls another function in the updateTransaction module called 
'resetTransactions' that resets all the customer transactions for the day and 
sets the excel sheet ready for the next day. Further explanation on how this function works
is explained in the updateTransaction file. 


'closeWindow' : This function essentially closes the window and logs the manager out of the home page. 

'''

class ManagerHomePage(Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        
        self.title('Manager HomePage')
        self.geometry('1000x500')
        self.config(bg = '#d9472a')


        self.logo = Image.open('pythonLogo.png')
        self.resized = self.logo.resize((310,200))
        self.logoNew = ImageTk.PhotoImage(self.resized)
        
        self.photoLabel = Label(self, image = self.logoNew,bg ='#d9472a')
        self.photoLabel.place(relx = 0.76,rely = 0.2,anchor = CENTER)



        
        #Frame for text and entry boxes
        self.homeFrame = Frame(self,pady = 75,padx = 75,bg = 'red')
        self.homeFrame.place(relx = 0.05,rely = 0.43,anchor = W)
        
        
        
        # Buttons to restock inventory and reset customer transactions
        self.button1 = customtkinter.CTkButton(self.homeFrame,text = 'Restock Inventory',command = self.resetInventory,
                                               bg_color='#d9472a',fg_color='black')
        self.button1.grid(row = 1,column = 0, columnspan = 2,pady = 3)
        
        self.button2 = customtkinter.CTkButton(self.homeFrame,text = 'Reset Transactions', command = self.resetTrans,
                                               bg_color='#d9472a',fg_color='black')
        self.button2.grid(row = 2,column = 0, columnspan = 2,pady = 3)

        
        # gets rev and put it in revenue label
        rev = getRevenue()
        rev = round(rev,2)
        
        self.label = customtkinter.CTkButton(self.homeFrame,text = 'Current Revenue: $'+str(rev),
                                            bg_color='#d9472a',fg_color='black',height = 20,width = 20)
        self.label.grid(row = 3,column = 0, columnspan = 2,pady = 3)
        
        
        
        # Exti button
        self.button4 = customtkinter.CTkButton(self,text = 'Exit',command = self.closeWindow,
                                               bg_color='#d9472a',fg_color='black')
        self.button4.place(relx = 0.8,rely = 0.8,anchor = W)
        
        
    def resetInventory(self):
        restockInventory()
        print('Inventory has been restocked!')
        messagebox.showinfo('Alert','Inventory has been restocked to full capacity')
         
    def resetTrans(self):
        resetTransactions()
        messagebox.showinfo('Alert','New excel sheet is now ready')
        
    def closeWindow(self): 
        self.withdraw()  
        from main import Main2
        Main2(self)
    
