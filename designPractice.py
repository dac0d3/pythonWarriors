from tkinter import *
import customtkinter
from tkinter import messagebox
from PIL import ImageTk,Image
import ttkbootstrap as tb


window = Tk()
window.geometry('1000x500')

logo = Image.open('pythonLogo.png')
resized = logo.resize((510,400))
logoNew = ImageTk.PhotoImage(resized)

photoLabel = Label(window, image = logoNew,bg ='#bf3c22')
photoLabel.place(relx = 0.5,rely = 0.5,anchor = CENTER)
#canvas = Canvas(window,height = 500,width = 500)

#redline = canvas.create_line(350,0,350,500,fill = 'red',width  = 5)
#rectangle = canvas.create_rectangle(45,40,500,500,fill = 'white',width = 10)
#blackline = canvas.create_line(10,50,500,50,fill = 'blue',width  = 5)

#canvas.pack()

text = Label(window,text = "I HOPE THIS WORKS",fg = 'black',bg = 'white')
text.place(relx = 0.5,rely = 0.5,anchor = CENTER)


window.mainloop()