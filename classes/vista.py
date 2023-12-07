import os.path
import sqlite3
from tkinter import *

import customtkinter as ctk
from CTkMessagebox.ctkmessagebox import CTkMessagebox
from PIL import Image
from App import App
from forgetPass import forget
import re


class LogIn(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.verify = None

        self.check_check = None
        self.no_label = None
        self.no_result = None
        self.show_button1 = None
        self.submit_add = None
        self.pass_add = None
        self.user_add = None
        self.email_add = None
        self.add_label = None
        self.add_frame = None
        self.add = None
        self.c = None
        self.conn = None
        self.title("")
        window_height = 500
        window_width = 900
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        self.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        self.iconbitmap('Pictures/icon.ico')
        self.geometry(f"{800}x{450}")
        self.resizable(0, 0)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.frame = ctk.CTkFrame(master=self)
        self.frame.grid(row=0,
                        column=2,
                        ipady=10,
                        padx=(20, 50),
                        pady=60)

        # PICTURES IMPORTINGGGGGGGGGGGGGGGGGGGGGG
        self.logo = ctk.CTkImage(dark_image=Image.open('Pictures/logoo.png'),
                                 size=(250, 100))
        self.logo_image = ctk.CTkLabel(self,
                                       image=self.logo,
                                       text="")
        self.logo_image.place(x=113,
                              y=165)
        self.logo1 = ctk.CTkImage(dark_image=Image.open('Pictures/2.png'),
                                  size=(55, 55))
        self.logo1_image = ctk.CTkLabel(self,
                                        image=self.logo1,
                                        text="")
        self.logo1_image.place(x=750,
                               y=395)
        fonty = ctk.CTkFont(family='Helvetica Neue')

        # ENTRY BOXES FOR LOG IN OR SIGN UPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
        self.email_entry = ctk.CTkEntry(self.frame,
                                        placeholder_text="  Username",
                                        placeholder_text_color='gray')
        self.email_entry.grid(row=0,
                              column=0,
                              ipadx=70,
                              ipady=5,
                              padx=10,
                              pady=10)
        self.pass_entry = ctk.CTkEntry(self.frame,
                                       placeholder_text="  Password",
                                       placeholder_text_color='gray',
                                       show='*')
        self.pass_entry.grid(row=1,
                             column=0,
                             ipadx=70,
                             ipady=5,
                             padx=10,
                             pady=(0, 10))
        self.eyes_close = ctk.CTkImage(dark_image=Image.open('Pictures/eye.png'),
                                       )
        self.eye_open = ctk.CTkImage(dark_image=Image.open('Pictures/view.png'),
                                     )
        self.eye = ctk.CTkButton(self.pass_entry,
                                 image=self.eyes_close,
                                 text="",
                                 corner_radius=0,
                                 fg_color='#343638',
                                 border_spacing=0,
                                 border_color='#343638',
                                 width=13,
                                 hover_color='#333434',
                                 border_width=0,
                                 command=self.show)
        self.eye.grid(column=0, row=0, sticky='e', padx=10)
        self.submit = ctk.CTkButton(self.frame,
                                    text='Log In',
                                    font=fonty,
                                    corner_radius=100,
                                    fg_color='#212121',
                                    hover_color='#1A1A1A',
                                    command=lambda: self.checker(self.email_entry.get(), self.pass_entry.get()))
        self.submit.grid(row=2,
                         column=0,
                         ipadx=10,
                         ipady=1,
                         )
        self.submit = ctk.CTkButton(self.frame,
                                    text='Forgot Password',

                                    fg_color='transparent',
                                    hover_color='#292929',
                                    font=ctk.CTkFont(size=11, weight="normal"),
                                    command=self.forgotPass)
        self.submit.grid(row=3,
                         column=0,
                         pady=(10, 0),
                         )
        self.separator = ctk.CTkLabel(self.frame, text="────────────────────",
                                      text_color='black'
                                      )
        self.separator.grid(row=4,
                            column=0,
                            )
        self.create = ctk.CTkButton(self.frame,
                                    text='Create new account',
                                    font=fonty,
                                    corner_radius=100,
                                    fg_color='#212121',
                                    hover_color='#1A1A1A',
                                    command=self.add_account)
        self.create.grid(row=5,
                         column=0,
                         )

    def forgotPass(self):
        self.adde = ctk.CTkToplevel(self)
        self.adde.iconbitmap('Pictures/icon.ico')
        self.adde.title("Options")
        self.adde.overrideredirect(True)
        window_height = 100
        window_width = 310
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        self.adde.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        self.adde.geometry("264x123")
        self.adde.grab_set()
        self.choicess = ctk.CTkFrame(self.adde)
        self.choicess.grid(row=5, column=0, )
        for i in range(0, 1):
            self.choicess.grid_columnconfigure(i, weight=0)
            self.choicess.grid_rowconfigure(i, weight=0)
        self.qna = ctk.CTkButton(self.choicess, text='       Question and answer', anchor='w', border_width=1,
                                 border_color='#3b3c3d', fg_color='#242526',
                                 font=ctk.CTkFont(size=12, weight="bold"), hover_color='#252e33',
                                 command=self.choice1)
        self.qna.grid(row=0, column=0, ipadx=59, sticky="w", ipady=8)
        self.verification_btn = ctk.CTkButton(self.choicess, text='       Email verification', anchor='w',
                                              border_width=1, border_color='#3b3c3d', fg_color='#242526',
                                              font=ctk.CTkFont(size=12, weight="bold"), hover_color='#252e33',
                                              command=self.choice2)
        self.verification_btn.grid(row=1, column=0, ipadx=70, sticky="w", ipady=8, )
        self.verification_btn2 = ctk.CTkButton(self.choicess, text='       Cancel', anchor='w',
                                               border_width=1, border_color='#3b3c3d', fg_color='#242526',
                                               font=ctk.CTkFont(size=12, weight="bold"), hover_color='#252e33',
                                               command=lambda: self.adde.destroy())
        self.verification_btn2.grid(row=2, column=0, ipadx=77, sticky="w", ipady=8, )

    def choice1(self):
        self.adde.destroy()
        return forget(1)

    def choice2(self):
        self.adde.destroy()
        return forget(2)

    def add_account(self):
        self.add = ctk.CTkToplevel(self)
        window_height = 300
        window_width = 430
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        self.add.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        self.add.geometry("325x235")
        self.add.title("CREATE ACCOUNT")
        self.add.grab_set()
        self.add_frame = ctk.CTkFrame(self.add, corner_radius=20)
        self.add_frame.pack(ipadx=50, ipady=50, padx=15, pady=15, )
        self.add_label = ctk.CTkLabel(self.add_frame,
                                      text="CREATE USER",
                                      font=('Arial', 30, 'bold'))
        self.add_label.pack(pady=10)
        self.email_add = ctk.CTkEntry(self.add_frame,
                                      placeholder_text="  Username",
                                      placeholder_text_color='gray')
        self.email_add.pack(pady=(5, 5), ipadx=70, ipady=6)
        self.pass_add = ctk.CTkEntry(self.add_frame,
                                     placeholder_text="  Password",
                                     placeholder_text_color='gray', show='*')
        self.eyes = ctk.CTkButton(self.pass_add,
                                  image=self.eyes_close,
                                  text="",
                                  corner_radius=0,
                                  fg_color='#343638',
                                  border_spacing=0,
                                  border_color='#343638',
                                  width=13,
                                  hover_color='#333434',
                                  border_width=0,
                                  command=self.show1)
        self.eyes.grid(column=0, row=0, sticky='e', padx=10)
        self.pass_add.pack(pady=(5, 5), ipadx=70, ipady=6)
        self.submit_add = ctk.CTkButton(self.add_frame,
                                        text='Add account',
                                        corner_radius=100,
                                        fg_color='#212121',
                                        hover_color='#1A1A1A',
                                        command=lambda: self.create_checker())
        self.submit_add.pack()

    # CREATINGG OF TABLESSSSSSSSSSSSSSSSSSSSSS AND TOP LEVEL ACCOUNTTTTTTTTTTTTTTTT
    def bullshet(self):
        msg = CTkMessagebox(title="Confirmation", message="Do you want to Continue?",
                            icon="question", option_1="Cancel", option_2="No", option_3="Yes")
        response = msg.get()
        if response == "Yes":
            self.conn = sqlite3.connect(f'{self.email_add.get()}.db')
            self.c = self.conn.cursor()
            with self.conn:
                self.c.execute("""CREATE TABLE IF NOT EXISTS user(
                                                   email TEXT,
                                                   password TEXT
                                                   )""")
            with self.conn:
                self.c.execute("""CREATE TABLE IF NOT EXISTS picture(
                                                   pictures BLOB
                                                   )""")
            with self.conn:
                self.c.execute("""CREATE TABLE IF NOT EXISTS files(
                                                   files BLOB
                                                   )""")
            with self.conn:
                self.c.execute("""CREATE TABLE IF NOT EXISTS notes(
                                                   title TEXT,
                                                   notes TEXT
                                                   )""")
            with self.conn:
                self.c.execute("""CREATE TABLE IF NOT EXISTS accounts(
                                                   acc_pass TEXT,
                                                   acc_name TEXT,
                                                   acc_email TEXT
                                                   )""")
            with self.conn:
                self.c.execute("""CREATE TABLE IF NOT EXISTS verify(
                                                   answer TEXT
                                                   )""")
            with self.conn:
                self.c.execute("""CREATE TABLE IF NOT EXISTS email(
                                                   email TEXT
                                                   )""")
            with self.conn:
                self.c.execute(
                    f"INSERT INTO user VALUES (:email, :password)",
                    {
                        'email': self.email_add.get(),
                        'password': self.pass_add.get()
                    })
            self.add.destroy()
        elif response == "No":
            self.email_add.delete(0, 'end')
            self.pass_add.delete(0, 'end')
        else:
            self.add.destroy()

    # SHOWING OF PASSWORD INPUTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
    def show(self):
        if self.pass_entry.cget('show') == '*':
            self.eye.configure(image=self.eye_open)
            self.pass_entry.configure(show='')

        else:
            self.eye.configure(image=self.eyes_close)
            self.pass_entry.configure(show='*')

    def show1(self):
        if self.pass_add.cget('show') == '*':
            self.pass_add.configure(show='')
            self.eyes.configure(image=self.eye_open)
        else:
            self.pass_add.configure(show='*')
            self.eyes.configure(image=self.eyes_close)

    # CHECKS ONLY IF ALL ENTRIES ON CREATING ACCOUNT IS FILLEDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
    def create_checker(self):
        username = self.email_add.get()
        password = self.pass_add.get()

        # password requirement
        if (
                len(password) >= 8
                and any(char.isdigit() for char in password)
                and any(char.isalpha() for char in password)
                and any(char.isupper() for char in password)
                and any(char.islower() for char in password)
                and re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)
        ):
            self.bullshet()
        else:
            CTkMessagebox(title="Error", message="Password should contain:" +
                                                 "\n   - 8 Characters" +
                                                 "\n   - Uppercase Letters" +
                                                 "\n   - Digits" +
                                                 "\n   - Special Characters", icon="cancel")

    def checker(self, check_one, check_2):
        if len(check_one) and len(check_2) != 0:
            return self.account_check()
        elif len(check_one) == 0:
            CTkMessagebox(title="Error", message="The username field is empty!!!", icon="cancel")
        elif len(check_2) == 0:
            CTkMessagebox(title="Error", message="The password field is empty!!!", icon="cancel")

    def account_check(self):
        self.check_check = f'{self.email_entry.get()}.db'
        self.state = os.path.exists(self.check_check)
        if self.state is True:
            return self.verification()
        else:
            msg = CTkMessagebox(title="Warning Message!", message="Coundn't find your Account!",
                                icon="warning", option_1="Cancel", option_2="Retry")
            if msg.get() == "Retry":
                self.email_entry.delete(0, 'end')
                self.pass_entry.delete(0, 'end')
            if msg.get() == "Cancel":
                return LogIn.destroy(self)

    def verification(self):
        self.conn = sqlite3.connect(f'{self.email_entry.get()}.db')
        self.c = self.conn.cursor()
        self.c.execute("SELECT password FROM user")
        keyntot = self.c.fetchone()
        for i in keyntot:
            self.verify = f"{i}"
        if self.verify == self.pass_entry.get():
            yow = self.email_entry.get()
            self.email_entry.delete(0, 'end')
            self.pass_entry.delete(0, 'end')
            return App(yow)
        else:
            msg = CTkMessagebox(title="Warning Message!",
                                message="The password you entered is incorrect. Please try again.",
                                icon="warning", option_1="Cancel", option_2="Retry")
            if msg.get() == "Retry":
                self.pass_entry.delete(0, 'end')
            if msg.get() == "Cancel":
                return LogIn.destroy(self)


##################################################################################################################################

##################################################################################################################################

##################################################################################################################################


if __name__ == "__main__":
    main = LogIn()
    main.mainloop()
