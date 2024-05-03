import unittest
from tkinter import Tk
from employeeSingIn import EmployeeSingIn, ChefSignIn, RunnerSignIn

class TestEmployeeSignIn(unittest.TestCase):
    
    def test_ChefSignIn_CorrectCredentials(self):
        root = Tk()
        app = ChefSignIn(root)
        app.entry1.insert(0, 'u')  
        app.entry2.insert(0, 'p')  
        app.checkInfo() 
        root.mainloop()  

    def test_ChefSignIn_IncorrectCredentials(self):
        root = Tk()
        app = ChefSignIn(root)
        app.entry1.insert(0, 'incorrect_username')  
        app.entry2.insert(0, 'incorrect_password') 
        app.checkInfo()  
        root.mainloop()  

    def test_RunnerSignIn_CorrectCredentials(self):
        root = Tk()
        app = RunnerSignIn(root)
        app.entry1.insert(0, 'u') 
        app.entry2.insert(0, 'p')  
        app.checkInfo()  
        root.mainloop()  

    def test_RunnerSignIn_IncorrectCredentials(self):
        root = Tk()
        app = RunnerSignIn(root)
        app.entry1.insert(0, 'incorrect_username') 
        app.entry2.insert(0, 'incorrect_password') 
        app.checkInfo()  

if __name__ == '__main__':
    unittest.main()
