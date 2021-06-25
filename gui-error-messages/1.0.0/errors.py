import os
import time
import random
from tkinter import *
def errormessage(text):
    time.sleep(0.05)
    root = Tk()
    #layout
    root.geometry("200x60")
    root.resizable(0, 0)
    root.title("Error")
    root.iconbitmap("C:/Users/johnm/OneDrive/Skrivebord/gui-error-messages/1.0.0/icons/error.ico")
    #internal
    mylabel = Label(root, text="There was an error\n" + text)
    mylabel.config(anchor=CENTER)
    mylabel.configure(font='Calibri 12')
    mylabel.pack()
    root.mainloop()
def crashmessage(text):
    time.sleep(0.05)
    root = Tk()
    # layout
    root.geometry("200x60")
    root.resizable(0, 0)
    root.title("Crash")
    root.iconbitmap("C:/Users/johnm/OneDrive/Skrivebord/gui-error-messages/1.0.0/icons/crash.ico")
    # internal
    mylabel = Label(root, text="Crash occured\n" + text)
    mylabel.config(anchor=CENTER)
    mylabel.configure(font='Calibri 12')
    mylabel.pack()
    root.mainloop()
def infomessage(text):
    time.sleep(0.05)
    root = Tk()
    # layout
    root.geometry("200x60")
    root.resizable(0, 0)
    root.title("Info")
    root.iconbitmap("C:/Users/johnm/OneDrive/Skrivebord/gui-error-messages/1.0.0/icons/info.ico")
    # internal
    mylabel = Label(root, text="Important\n" + text)
    mylabel.config(anchor=CENTER)
    mylabel.configure(font='Calibri 12')
    mylabel.pack()
    root.mainloop()
