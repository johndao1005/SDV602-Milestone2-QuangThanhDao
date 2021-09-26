import tkinter as tk
from tkinter import ttk


datasource = "./data-sample/test.csv"
app_name = "White shark tracking"
pad20 = {'padx': 20, 'pady': 20}
pad10 = {'padx': 10, 'pady': 10}
pad5 = {'padx': 5, 'pady': 5}
icon = "./src/wireshark.ico"

class PageOne(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Page One")
        label.pack(pady=10,padx=10)
        #button1 = ttk.Button(self, text ="Back To Home",