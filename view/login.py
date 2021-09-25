#import view.ChartExamples as ce 
import controller.exit_button as exit_button
#import controller.DES.figure_list_select as figure_list_select
from controller.login import login
import PySimpleGUI as sg
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk
import setup

class App(Tk):
    def __init__(self):
        """Start an instance of login screen which allow user to sign up with top level window or login directly
        When users login, the class would open to menu which is another class which handle the data view, update, delete while
        destroy the current login to prevent multiple login.
        """
        super().__init__()
        self.title(setup.app_name)
        self.iconbitmap(setup.icon)
        options = setup.pad10
        option2 = setup.pad5
        self.resizable(0, 0)
        label = Label(self, text="Login").grid(column=0,row=0,sticky=N,**options,columnspan=3)
        self.geometry("280x250+200+300")
        self.check = False
        # ANCHOR data input
        lf = Frame(
        self,
        ).grid(column=0, row=0, padx=10, pady=0)
        password = StringVar()
        username = StringVar()
        label = ttk.Label(lf, text="Username").grid(column=0,row=1,**options,ipadx=5, ipady=5)
        username_entry = Entry(lf, textvariable=username).grid(column=1,row=1,**options,columnspan=2)
        label = ttk.Label(lf, text="Password").grid(column=0,row=2,**options,ipadx=5, ipady=5)
        password_entry = Entry(lf, textvariable=password, show="*").grid(column=1,row=2,**options,columnspan=2)
        # ANCHOR Buttons for main window
        button_frame = ttk.Frame(
        self,
        ).grid(column=1, row=1, padx=10, pady=10)
        login_btn = ttk.Button(button_frame,
                           text="Login",
                           command=lambda: login(username,password)
                           ).grid(column=1,row=3,**option2)
        signup_btn = ttk.Button(button_frame,
                            text="Sign Up",
                            command=lambda: self.call_signup()
                            ).grid(column=2,row=3,**option2)
        quit_btn = ttk.Button(self,
                          text="Quit",
                          command=lambda: self.destroy()
                          ).grid(column=2,row=4,**options)
        
        def call_signup(self):
            """The function check for any instance of signup and only create a sign up window if there is none
        """
        if self.check == False:
            self.signup_window()