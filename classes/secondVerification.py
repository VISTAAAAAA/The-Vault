import sqlite3

import customtkinter as ctk
from CTkMessagebox.ctkmessagebox import CTkMessagebox

from emailVerification import emailVer


class bros(ctk.CTkToplevel):
    def __init__(self, mail):
        super().__init__()
        window_height = 400
        window_width = 550
        self.resizable(0, 0)
        self.overrideredirect(True)
        self.grab_set()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        self.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        self.acc_frame = None
        self.mail = mail

        global pew
        pew = self.conn = sqlite3.connect(f'{mail}.db')
        self.title('AUTHENTICATION')
        self.geometry("470x360")
        self.grab_set()

        self.add_frame = ctk.CTkFrame(self, fg_color='#202020', corner_radius=20)
        self.add_frame.pack(ipadx=100, ipady=100)
        self.titles = ctk.CTkLabel(self.add_frame,
                                   text="Authentication",
                                   font=('Arial', 30, 'bold'))
        self.titles.pack(anchor='w', pady=(60, 15), padx=20)
        self.separator = ctk.CTkLabel(self.add_frame, text="───────────────────────────────────────",
                                      text_color='black'
                                      )
        self.separator.pack()

        self.email = emailVer()
        self.code = self.email.generate_random_code()

        self.description = ctk.CTkLabel(self.add_frame,
                                        text="Email Authentication",
                                        font=('Arial', 20, 'bold')
                                        )
        self.description.pack()
        self.titles = ctk.CTkLabel(self.add_frame,
                                   text="Enter your email address.",
                                   font=('Arial', 11, 'bold'))
        self.titles.pack(pady=10)
        self.searchAcc1 = ctk.CTkEntry(self.add_frame,
                                       placeholder_text="  Email Address",
                                       placeholder_text_color='gray',
                                       border_color='#303030'
                                       )
        self.searchAcc1.pack(ipadx=50, ipady=6)
        self.separator = ctk.CTkLabel(self.add_frame, text="───────────────────────────────────",
                                      text_color='black'
                                      )
        self.separator.pack()
        self.cancel = ctk.CTkButton(self.add_frame,
                                    text='  Submit',
                                    corner_radius=100,
                                    fg_color='#212121',
                                    hover_color='#1A1A1A',
                                    command=lambda: [f() for f in [self.gen_code, self.codeConfirm]]
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

    def gen_code(self):
        self.email_instance = emailVer()
        self.code = self.email_instance.generate_random_code()
        self.email_instance.send_email(self.searchAcc1.get(), self.code)

    def codeConfirm(self):
        self.confirm = ctk.CTkToplevel(self)
        self.confirm.title('CODE VERIFICATION')
        self.confirm.overrideredirect(True)
        self.confirm.grab_set()
        window_height = 300
        window_width = 250
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        self.confirm.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        self.confirm.geometry("350x220")
        self.codeDescription = ctk.CTkLabel(self.confirm,
                                            text="Code Confirmation",
                                            font=('Arial', 20, 'bold')
                                            )
        self.codeDescription.pack(pady=10)
        self.titles = ctk.CTkLabel(self.confirm,
                                   text="Enter your code.",
                                   font=('Arial', 11, 'bold'))
        self.titles.pack(pady=10)
        self.userCode = ctk.CTkEntry(self.confirm,
                                     placeholder_text="  CODE",
                                     placeholder_text_color='gray',
                                     border_color='#303030'
                                     )
        self.userCode.pack(ipadx=50, ipady=6)
        self.separator = ctk.CTkLabel(self.confirm, text="───────────────────────────────────",
                                      text_color='black'
                                      )
        self.separator.pack()
        self.cancel = ctk.CTkButton(self.confirm,
                                    text='  Submit',
                                    corner_radius=100,
                                    fg_color='#212121',
                                    hover_color='#1A1A1A',
                                    command=self.confirmCode
                                    )
        self.cancel.pack(side='right', anchor='nw')
        self.submit = ctk.CTkButton(self.confirm,
                                    text='  Cancel',
                                    corner_radius=100,
                                    fg_color='#212121',
                                    hover_color='#1A1A1A',
                                    command=self.cancel1
                                    )
        self.submit.pack(side='right', anchor='nw')

    def confirmCode(self):
        if self.userCode.get() == self.code:
            self.conn = pew
            self.c = self.conn.cursor()
            with self.conn:
                self.c.execute(f"INSERT INTO email VALUES (:email)",
                               {
                                   'email': self.searchAcc1.get()
                               })
            return bros.destroy(self)
        else:
            msg = CTkMessagebox(title="Warning Message!", message="The verification code you entered is incorrect.",
                                icon="warning", option_1="Cancel", option_2="Retry")
            if msg.get() == "Retry":
                self.userCode.delete(0, 'end')
            if msg.get() == "Cancel":
                return bros.destroy(self)



    def cancel1(self):
        return self.destroy()






