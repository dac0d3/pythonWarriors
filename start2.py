from tkinter import *
import customtkinter
from tkinter import messagebox
from PIL import ImageTk,Image
import ttkbootstrap as tb


from main import *

'''




'''

def start():
    run = Main()
    if run.wm_state == 'withdrawn':
        run.iconify()
    run.mainloop()
    
start() 