


def upload_window(self,user="user"):
        self.upload = Toplevel()
        self.upload.title(setup.app_name)
        self.upload.iconbitmap(setup.icon)
        option2 = setup.pad10
        option1 = setup.pad5
        label = Label(self.upload, text="New Data").grid(column=0,row=0,**option2)
        self.upload.geometry("440x320")
        self.upload.protocol("WM_DELETE_WINDOW",self.close_upload)
        label = Label(self.upload, text=f"Thank you {user}, please fill the details below for new entry.\n We can use your current location or you can manual input your coordinate").grid(column=0,row=1,**option1)
        gender = StringVar()
        feature = StringVar()
        note = StringVar()
        locationX = StringVar()
        locationY = StringVar()
        # Creating entry box
        lf = ttk.LabelFrame(self.upload,text ="Insert data below")
        lf.grid(column=0,row=2,**option2)
        label = ttk.Label(lf, text="Gender").grid(column=0,row=3,**option1)
        username_entry = ttk.Entry(lf,text="Gender", textvariable=gender).grid(column=1,row=3,**option1)
        label = ttk.Label(lf, text="feature").grid(column=2,row=3,**option1)
        password_entry = ttk.Entry(lf, textvariable=feature).grid(column=3,row=3,**option1)
        label = ttk.Label(lf, text="LocationX").grid(column=0,row=4,**option1)
        email_entry = ttk.Entry(lf, textvariable=locationX).grid(column=1,row=4,**option1)
        label = ttk.Label(lf, text="LocationY").grid(column=2,row=4,**option1)
        email_entry = ttk.Entry(lf, textvariable=locationY).grid(column=3,row=4,**option1)
        label = ttk.Label(lf, text="Note").grid(column=0,row=6,**option1)
        confirmpassword_entry = ttk.Entry(lf, textvariable=note).grid(column=1,row=6,**option1)
        self.upload_Btn = ttk.Button(lf, text="Upload",
                        command=lambda: self.upload_data()).grid(column=0,row=8,**option2,columnspan=4)
        cancel_Btn = ttk.Button(self.upload, text="Cancel",
                        command=lambda: self.close_upload()).grid(column=0,row=9,**option2,sticky=SE)
        self.upload.mainloop()