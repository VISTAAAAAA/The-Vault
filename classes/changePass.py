import os
from tkinter import *
from CTkMessagebox.ctkmessagebox import CTkMessagebox
import customtkinter as ctk
from PIL import Image
import sqlite3


class changePass(ctk.CTkToplevel):
    def __init__(self, mail):
        super().__init__()
        window_height = 400
        self.overrideredirect(True)
        self.resizable(0, 0)
        window_width = 550
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        self.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        self.acc_frame = None
        self.mail = mail
        global pew
        pew = self.conn = sqlite3.connect(f'{mail}.db')
        self.title('RESET PASSWORD')
        self.geometry("470x360")
        self.grab_set()
        self.add_frame = ctk.CTkFrame(self, fg_color='#202020', corner_radius=20)
        self.add_frame.pack(ipadx=100, ipady=100)
        self.titles = ctk.CTkLabel(self.add_frame,
                                   text="Choose a new password",
                                   font=('Arial', 30, 'bold'))
        self.titles.pack(anchor='w', pady=(60, 15), padx=20)
        self.separator = ctk.CTkLabel(self.add_frame, text="───────────────────────────────────────",
                                      text_color='black'
                                      )
        self.separator.pack()
        self.description = ctk.CTkLabel(self.add_frame,
                                        text="Create a new password that is at least 6 \ncharacters long. A strong "
                                             "password is combination of \nletters, numbers, and punctuation marks.",
                                        font=('Arial', 11, 'bold')
                                        )
        self.description.pack()
        self.eyes_close = ctk.CTkImage(dark_image=Image.open('Pictures/eye.png'),
                                       )
        self.eye_open = ctk.CTkImage(dark_image=Image.open('Pictures/view.png'),
                                     )
        self.searchAcc0 = ctk.CTkEntry(self.add_frame,
                                      placeholder_text="  New password",
                                      placeholder_text_color='gray',
                                      border_color='#303030',
                                       show='*'
                                      )
        self.searchAcc0.pack(ipadx=50, ipady=6)
        self.eye3 = ctk.CTkButton(self.searchAcc0,
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
        self.eye3.grid(column=0, row=0, sticky='e', padx=10)
        self.separator = ctk.CTkLabel(self.add_frame, text="───────────────────────────────────",
                                      text_color='black'
                                      )
        self.separator.pack()
        self.cancel = ctk.CTkButton(self.add_frame,
                                    text='  Continue',
                                    corner_radius=100,
                                    fg_color='#212121',
                                    hover_color='#1A1A1A',
                                    command=lambda: self.searchAcc2()
                                    )
        self.cancel.pack(side='right', anchor='nw')
        self.submit = ctk.CTkButton(self.add_frame,
                                    text='  Cancel',
                                    corner_radius=100,
                                    fg_color='#212121',
                                    hover_color='#1A1A1A',
                                    command=self.cancel1
                                    )
        self.submit.pack(side='right', anchor='nw')

    def show(self):
        if self.searchAcc0.cget('show') == '*':
            self.eye3.configure(image=self.eye_open)
            self.searchAcc0.configure(show='')
        else:
            self.eye3.configure(image=self.eyes_close)
            self.searchAcc0.configure(show='*')

    def cancel1(self):
        return self.destroy()

    def searchAcc2(self):
        if len(self.searchAcc0.get()) != 0:
            self.check_check = f'{self.mail}.db'
            self.state = os.path.exists(self.check_check)
            if self.state is True:
                self.conn = sqlite3.connect(f'{self.mail}.db')
                self.c = self.conn.cursor()
                with self.conn:
                    self.c.execute("""UPDATE user SET password = :password""", {
                        'password': self.searchAcc0.get()})
                return changePass.destroy(self)

            else:
                msg = CTkMessagebox(title="Warning Message!", message="Coundn't find your Account!",
                                    icon="warning", option_1="Cancel", option_2="Retry")
                if msg.get() == "Retry":
                    self.searchAcc0.delete(0, 'end')
                if msg.get() == "Cancel":
                    return changePass.destroy(self)

        else:
            CTkMessagebox(title="Error", message="The new password field is empty!!!",
                          icon="cancel")
