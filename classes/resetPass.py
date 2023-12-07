from CTkMessagebox.ctkmessagebox import CTkMessagebox
import customtkinter as ctk
import sqlite3
from changePass import changePass

class resets(ctk.CTkToplevel):
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
        self.description = ctk.CTkLabel(self.add_frame,
                                        text="Who is your child hood best friend?",
                                        font=('Arial', 20, 'bold')
                                        )
        self.description.pack()
        self.titles = ctk.CTkLabel(self.add_frame,
                                   text="Answer the questions from your heart.",
                                   font=('Arial', 11, 'bold'))
        self.titles.pack(pady=10)
        self.searchAcc = ctk.CTkEntry(self.add_frame,
                                      placeholder_text="  Answer",
                                      placeholder_text_color='gray',
                                      border_color='#303030'
                                      )
        self.searchAcc.pack(ipadx=50, ipady=6)
        self.separator = ctk.CTkLabel(self.add_frame, text="───────────────────────────────────",
                                      text_color='black'
                                      )
        self.separator.pack()
        self.cancel = ctk.CTkButton(self.add_frame,
                                    text='  Search',
                                    corner_radius=100,
                                    fg_color='#212121',
                                    hover_color='#1A1A1A',
                                    command=self.searchAcc2
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

    def cancel1(self):
        return self.destroy()

    def searchAcc2(self):
        if len(self.searchAcc.get()) != 0:
            self.conn = sqlite3.connect(f'{self.mail}.db')
            self.c = self.conn.cursor()
            with self.conn:
                self.c.execute("SELECT answer FROM verify")
                keyntot = self.c.fetchall()
                f = 0
            for i in keyntot:
                self.verify = f"{i[f]}"
                if self.verify == self.searchAcc.get():
                    changePass(self.mail)
                    return resets.destroy(self)

        else:
            msg = CTkMessagebox(title="Warning Message!", message="Coundn't find your Account!",
                                icon="warning", option_1="Cancel", option_2="Retry")
            if msg.get() == "Retry":
                self.searchAcc.delete(0, 'end')
            if msg.get() == "Cancel":
                return resets.destroy(self)