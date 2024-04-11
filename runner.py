# runner delivers order 
# order is confirmed 

from tkinter import *
import openpyxl
from openpyxl import Workbook, load_workbook



class Runner(Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        
        self.title('Runner GUI')
        self.geometry('1400x500')