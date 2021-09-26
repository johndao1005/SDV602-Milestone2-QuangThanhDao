import controller.exit_button as exit_button
from controller.login.auth import authentication
from tkinter import ttk
import view.setup as setup
import view.signup as Signup
import tkinter as tk


class Login(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        options = setup.pad10
        option2 = setup.pad5
        label = tk.Label(self, text="Login").grid(column=0,row=0,sticky="N",**options,columnspan=3)
        #parent.geometry("280x250+200+300")
        self.check = False
        # ANCHOR data input
        lf = ttk.Frame(
        self,
        ).grid(column=0, row=0, padx=10, pady=0)
        password = tk.StringVar()
        username = tk.StringVar()
        label = ttk.Label(lf, text="Username").grid(column=0,row=1,**options,ipadx=5, ipady=5)
        username_entry = ttk.Entry(lf, textvariable=username).grid(column=1,row=1,**options,columnspan=2)
        label = ttk.Label(lf, text="Password").grid(column=0,row=2,**options,ipadx=5, ipady=5)
        password_entry = ttk.Entry(lf, textvariable=password, show="*").grid(column=1,row=2,**options,columnspan=2)
        # ANCHOR Buttons for main window
        button_frame = ttk.Frame(
        self,
        ).grid(column=1, row=1, padx=10, pady=10)
        login_btn = ttk.Button(button_frame,
                           text="Login",
                           command=lambda: authentication(self,username,password)
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
        if self.check == False:
            Signup()