from controller.login.register import makeUser
from tkinter import ttk
from controller.exit_button import closeToplevel
import view.setup as setup
import tkinter as tk



class Signup(tk.Toplevel):
    def __init__(self, parent, controller):
        super().__init__()
        parent.check = True
        self.title(setup.app_name)
        self.iconbitmap(setup.icon)
        options = {'padx': 10, 'pady': 5}
        label = ttk.Label(self, text="Sign up").grid(
            column=0, row=0, **options, columnspan=2)
        self.geometry("310x360+100+100")
        self.protocol("WM_DELETE_WINDOW", closeToplevel(parent))
        # Create placeholder to store data
        username = tk.StringVar()
        password = tk.StringVar()
        confirmPassword = tk.StringVar()
        email = tk.StringVar()
        lf = ttk.LabelFrame(self, text="Login details")
        lf.grid(column=0, row=1, padx=20, pady=20)
        label = ttk.Label(lf, text="Username").grid(column=0, row=3, **options)
        username_entry = ttk.Entry(lf, textvariable=username).grid(
            column=1, row=3, **options)
        username_check = ttk.Label(lf, text="").grid(column=1, row=4)
        label = ttk.Label(lf, text="Pass word").grid(
            column=0, row=5, **options)
        password_entry = ttk.Entry(lf, textvariable=password).grid(
            column=1, row=5, **options)
        password_check = ttk.Label(lf, text="").grid(column=1, row=6)
        label = ttk.Label(lf, text="Confirm Password").grid(
            column=0, row=7, **options)
        confirmpassword_entry = ttk.Entry(
            lf, textvariable=confirmPassword).grid(column=1, row=7, **options)
        confirm_password_check = ttk.Label(lf, text="").grid(column=1, row=8)
        label = ttk.Label(lf, text="Email").grid(column=0, row=9, **options)
        email_entry = ttk.Entry(lf, textvariable=email).grid(
            column=1, row=9, **options)
        email_check = ttk.Label(lf, text="").grid(column=1, row=10)
        button = ttk.Button(lf,
                            text="Sign Up",
                            command=lambda: makeUser(
                                username, password, confirmPassword, email)
                            ).grid(column=0, row=11, **options, columnspan=2)
        button = ttk.Button(self,
                            text="Cancel",
                            command=lambda: closeToplevel(parent)
                            ).grid(column=0, row=3, **options, sticky="SE")
        self.mainloop()
