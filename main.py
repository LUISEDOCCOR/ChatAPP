import localdb as ldb
import signup
import login
from tkinter import messagebox
#import chatapp

def Chatapp():
    #chatapp.app()        
    pass


x = ldb.isNotLogin
if x:
    y = messagebox.askquestion('Chat APP', 'Do you have account?')
    if y == 'yes':
        login.GUILOGIN()   
    else:
        signup.GUISIGNUP()

else:
    Chatapp()
    

