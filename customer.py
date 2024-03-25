#name   #email   #confirm button takes to order file


from tkinter import *


#name = 'customer'
#email = 'email@abc.com'

window = Tk()
window.geometry('1440x900')
window.title('Customer Registration')


# gets values for name and email from customer when confirm button is clicked 
def getVals():
    nameVal = nameEntry.get()
    emailVal = emailEntry.get()
    nameEntry.config(state = DISABLED)
    emailEntry.config(state = DISABLED)
    print(nameVal,emailVal)
    window.destroy()             #close window here 
    from order import Order_Menu #  <-- call class for order here
    
    
    
    

#Heading 
Label(window,text = "Customer Registration",font = 'ar 20 bold').grid(row = 0,column = 3)


#Field Name
name = Label(window,text = "Name")
email = Label(window,text = "Email")


#Packing Fields
name.grid(row = 1,column = 2)
email.grid(row = 2,column = 2)


#Var for storing data
nameVal = StringVar
emailVal = StringVar
checkVar = IntVar


#Creating Entry Field
nameEntry = Entry(window,textvariable=nameVal)
emailEntry = Entry(window,textvariable=emailVal)


#Packing Entry Fields
nameEntry.grid(row = 1,column = 3)
emailEntry.grid(row = 2,column = 3)


#Submit Button
Button(window,text = 'Submit',command = getVals).grid(row = 7,column = 3)


window.mainloop()

