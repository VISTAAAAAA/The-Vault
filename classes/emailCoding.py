from CTkMessagebox.ctkmessagebox import CTkMessagebox
import customtkinter as ctk
import sqlite3
from changePass import changePass
from emailVerification import emailVer


class rere(ctk.CTkToplevel):
    def __init__(self, mail):
        super().__init__()
        global pew
        pew = self.conn = sqlite3.connect(f'{mail}.db')
        self.grab_set()
        self.mail = mail
        self.title('CODE VERIFICATION')
        self.overrideredirect(True)
        window_height = 280
        window_width = 50
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        self.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        self.geometry("350x220")
        self.meoww = ctk.CTkFrame(self, fg_color='#202020', corner_radius=20)
        self.meoww.pack(ipadx=100, ipady=100)
        self.email = emailVer()
        self.code = self.email.generate_random_code()
        self.email_instance = emailVer()
        self.code = self.email_instance.generate_random_code()
        self.c = self.conn.cursor()
        with self.conn:
            self.c.execute("SELECT email FROM email")
            keyntot = self.c.fetchall()
            f = 0
        for i in keyntot:
            self.verify = f"{i[f]}"
        self.email_instance.send_email(self.verify, self.code)
        self.codeDescription = ctk.CTkLabel(self.meoww,
                                            text="Code Confirmation",
                                            font=('Arial', 20, 'bold')
                                            )
        self.codeDescription.pack(pady=10)
        self.titles = ctk.CTkLabel(self.meoww,
                                   text="Enter your code.",
                                   font=('Arial', 11, 'bold'))
        self.titles.pack(pady=10)
        self.userCode = ctk.CTkEntry(self.meoww,
                                     placeholder_text="  CODE",
                                     placeholder_text_color='gray',
                                     border_color='#303030'
                                     )
        self.userCode.pack(ipadx=50, ipady=6)

        self.separator = ctk.CTkLabel(self.meoww, text="───────────────────────────────────",
                                      text_color='black'
                                      )
        self.separator.pack()
        self.cancel = ctk.CTkButton(self.meoww,
                                    text='  Submit',
                                    corner_radius=100,
                                    fg_color='#212121',
                                    hover_color='#1A1A1A',
                                    command=self.confirmCode
                                    )
        self.cancel.pack(side='right', anchor='nw')
        self.submit = ctk.CTkButton(self.meoww,
                                    text='  Cancel',
                                    corner_radius=100,
                                    fg_color='#212121',
                                    hover_color='#1A1A1A',
                                    command=self.cancel1
                                    )
        self.submit.pack(side='right', anchor='nw')

    def confirmCode(self):
        if self.userCode.get() == self.code:
            changePass(self.mail)
            return self.destroy()
        else:
            msg = CTkMessagebox(title="Warning Message!", message="The verification code you entered is incorrect.",
                                icon="warning", option_1="Cancel", option_2="Retry")
            if msg.get() == "Retry":
                self.userCode.delete(0, 'end')
            if msg.get() == "Cancel":
                return rere.destroy(self)

    def cancel1(self):
        return self.destroy()