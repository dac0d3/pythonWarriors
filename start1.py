
from tkinter import *
import customtkinter
from tkinter import messagebox
from PIL import ImageTk,Image
import ttkbootstrap as tb
import time

from openKiosk import *

'''




'''

def start():
    

    run = CustomerTransaction()
    if run.wm_state == 'withdrawn':
        run.iconify()
    run.mainloop()
    
start() 
