import openKiosk
import unittest

import unittest
from tkinter import Tk
from openKiosk import CustomerTransaction2

class TestopenCustomerTransactions(unittest.TestCase):
    
    def test_CustomerTransaction2(self):
        root = Tk()
        app = CustomerTransaction2()
        app.startTransaction()  
        root.mainloop()  

if __name__ == '__main__':
    unittest.main()
