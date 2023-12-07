import io
from tkinter import *
from tkinter import filedialog
from CTkMessagebox.ctkmessagebox import CTkMessagebox
import customtkinter as ctk

from PIL import Image, ImageTk
import sqlite3
from secondVerification import bros



class App(ctk.CTkToplevel):
    def __init__(self, email):
        super().__init__()
        self.verification_btn = None
        self.settings = None
        self.iconbitmap('Pictures/icon.ico')
        self.height_pic = None
        self.width_pic = None
        self.grab_set()
        self.scrollable_notes_switches = None
        self.image_database = None
        self.account_add = None
        self.show_label = None
        self.name = None
        self.row = None
        self.scrollable_account_switches = None
        self.show_account = None
        self.show = None
        self.index_num = None
        self.col = 0
        self.num = None
        self.acc = None
        self.show_acc = None
        self.pass_add = None
        self.scrollable_notes = None
        self.scrollable_acc = None
        self.submit_add = None
        self.scrollable_picture_switches = None
        self.scrollable_picture = None
        self.pictures = None
        self.pictures_frame = None
        self.files = None
        self.add_file2 = None
        self.files_frame = None
        self.add_file1 = None
        self.add_file3 = None
        self.notes = None
        self.add_file = None
        self.notes_frame = None
        self.sum = 1
        self.email = email
        window_height = 600
        window_width = 1200
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        self.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        self.acc_frame = None
        self.title('THE VAULT')
        self.geometry("1100x580")
        self.grab_set()
        self.conn = sqlite3.connect(f'{email}.db')
        self.c = self.conn.cursor()
        global pew
        pew = self.conn = sqlite3.connect(f'{email}.db')
        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=0)
        self.grid_rowconfigure((0, 2), weight=1)
        self.grid_rowconfigure(1, weight=65)

        # create sidebar frame with widgets
        self.sidebar_frame = ctk.CTkFrame(self, fg_color='#202020', width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=1)

        # pictures import
        self.logo = ctk.CTkImage(dark_image=Image.open('Pictures/logoo.png'),
                                 size=(100, 50))
        self.one = ctk.CTkImage(dark_image=Image.open('Pictures/picture.png'),
                                size=(20, 20))

        self.three = ctk.CTkImage(dark_image=Image.open('Pictures/notes.png'),
                                  size=(20, 20))
        self.four = ctk.CTkImage(dark_image=Image.open('Pictures/account.png'),
                                 size=(20, 20))
        self.five = ctk.CTkImage(dark_image=Image.open('Pictures/setting.png'),
                                 size=(20, 20))
        self.logo_upper = ctk.CTkImage(dark_image=Image.open('Pictures/up.png'),
                                       size=(30, 30))
        self.plus = ctk.CTkImage(dark_image=Image.open('Pictures/plus.png'),
                                 size=(40, 40))

        self.logo_label = ctk.CTkLabel(self.sidebar_frame,
                                       text="",
                                       image=self.logo,
                                       font=ctk.CTkFont(size=30, weight="bold"))
        self.logo_label.grid(row=0,
                             column=0,
                             padx=(20, 5),
                             pady=(10, 10))
        self.sidebar_button_1 = ctk.CTkButton(self.sidebar_frame,
                                              text="Pictures",
                                              image=self.one,
                                              command=self.pictures_button_event)
        self.sidebar_button_1.grid(row=1,
                                   column=0,
                                   padx=20,
                                   pady=10)

        self.sidebar_button_3 = ctk.CTkButton(self.sidebar_frame,
                                              text="Notes",
                                              image=self.three,
                                              command=self.notes_button_event)
        self.sidebar_button_3.grid(row=3,
                                   column=0,
                                   padx=20,
                                   pady=10)
        self.sidebar_button_4 = ctk.CTkButton(self.sidebar_frame,
                                              text="Accounts",
                                              image=self.four,
                                              command=self.account_button_event)
        self.sidebar_button_4.grid(row=4,
                                   column=0,
                                   padx=20,
                                   pady=10)
        self.sidebar_button_5 = ctk.CTkButton(self.sidebar_frame,
                                              text="Settings",
                                              image=self.five,
                                              command=self.settingss)
        self.sidebar_button_5.grid(row=10,
                                   column=0,
                                   padx=20,
                                   pady=10)
        self.scaling_label = ctk.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=8, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame,
                                                     values=["80%", "90%", "100%", "110%", "120%"],
                                                     command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=9, column=0, padx=20, pady=(10, 10))
        #####################################################################################################

        # Upper Frame

        self.upper_frame = ctk.CTkFrame(self, fg_color='#202020', width=180, corner_radius=0)
        self.upper_frame.grid(row=0, column=1, columnspan=2, sticky="nsew")
        self.upper_frame.grid_columnconfigure(1, weight=1)
        self.upper_frame.grid_columnconfigure(2, weight=1)

        self.logo_up = ctk.CTkLabel(self.upper_frame,
                                    text="",
                                    image=self.logo_upper,
                                    font=ctk.CTkFont(size=30, weight="bold"))
        self.logo_up.grid(row=0, column=2, columnspan=1, pady=(20, 20), )

        self.account = ctk.CTkLabel(self.upper_frame, text=email.capitalize(), font=('Arial', 25))
        self.account.grid(row=0, column=2, columnspan=1, padx=(80, 20), pady=(20, 20), )
        self.entry = ctk.CTkEntry(self.upper_frame, fg_color='#202020', placeholder_text="Search")
        self.entry.grid(row=0, column=0, ipadx=250, columnspan=2, padx=(20, 20), pady=(20, 20), sticky="e")

    ##################################################################################################################
    def settingss(self):
        self.settings = ctk.CTkScrollableFrame(self, width=140, label_text="Settings")
        self.settings.grid(row=1, column=1, columnspan=2, rowspan=2, sticky="nsew")
        for i in range(0, 6):
            self.settings.grid_columnconfigure(i, weight=1)
            self.settings.grid_rowconfigure(i, weight=1)
        self.verification_label1 = ctk.CTkLabel(self.settings, text="Password and security",
                                                font=ctk.CTkFont(size=30, weight="bold"))
        self.verification_label1.grid(row=0, column=2, sticky="w", pady=(0, 20))

        self.verification_label2 = ctk.CTkLabel(self.settings, text="Login & recovery",
                                                font=ctk.CTkFont(size=15, weight="bold"), )
        self.verification_label2.grid(row=1, column=2, sticky="w", pady=(5, 0))
        self.verification_label3 = ctk.CTkLabel(self.settings,
                                                text="Manage your passwords, login preferences and recovery methods.",
                                                )
        self.verification_label3.grid(row=2, column=2, sticky="w", pady=(0, 15))

        self.change_btn = ctk.CTkButton(self.settings, text='       Change password', anchor='w', border_width=1,
                                        border_color='#3b3c3d', fg_color='#242526',
                                        font=ctk.CTkFont(size=12, weight="bold"), hover_color='#252e33',
                                        command=self.changePass)
        self.change_btn.grid(row=3, column=2, ipadx=251, sticky="w", ipady=8)
        self.verification_btn = ctk.CTkButton(self.settings, text='       Two-factor authentication', anchor='w',
                                              border_width=1, border_color='#3b3c3d', fg_color='#242526',
                                              font=ctk.CTkFont(size=12, weight="bold"), hover_color='#252e33',
                                              command=self.choiceshehe)
        self.verification_btn.grid(row=4, column=2, ipadx=219, sticky="w", ipady=8, pady=(0, 20))

    def changePass(self):
        self.add = ctk.CTkToplevel(self)
        self.add.geometry("340x325")
        self.add.title('Change Password')
        self.add.resizable(0, 0)
        self.add.grab_set()
        self.add_frame = ctk.CTkFrame(self.add)
        self.add_frame.grid(row=5, column=0, ipady=25, padx=10, pady=10)
        for i in range(0, 5):
            self.add_frame.grid_columnconfigure(i, weight=0)
            self.add_frame.grid_rowconfigure(i, weight=1)
        self.titles = ctk.CTkLabel(self.add_frame,
                                   text="Change Password",
                                   font=('Arial', 30, 'bold'))
        self.titles.grid(row=0,
                         column=0,
                         )
        self.description = ctk.CTkLabel(self.add_frame,
                                        text="Your password must be at least 6 characters to be strong"
                                        )
        self.description.grid(row=1,
                              column=0,
                              )
        self.currentPass = ctk.CTkEntry(self.add_frame,
                                        placeholder_text="  Current password",
                                        placeholder_text_color='gray',
                                        show='*')
        self.currentPass.grid(row=2,
                              column=0,
                              ipadx=70,
                              ipady=5,
                              padx=15,
                              pady=5)
        self.newPass = ctk.CTkEntry(self.add_frame,
                                    placeholder_text="  New password",
                                    placeholder_text_color='gray',
                                    show='*')
        self.newPass.grid(row=3,
                          column=0,
                          ipadx=70,
                          ipady=5,
                          padx=15,
                          pady=5)
        self.retype = ctk.CTkEntry(self.add_frame,
                                   placeholder_text="  Re-type new password",
                                   placeholder_text_color='gray',
                                   show='*')
        self.retype.grid(row=4,
                         column=0,
                         ipadx=70,
                         ipady=5,
                         padx=15,
                         pady=5)
        self.submit_add = ctk.CTkButton(self.add_frame,
                                        text='  Change password',
                                        corner_radius=100,
                                        fg_color='#212121',
                                        hover_color='#1A1A1A',
                                        command=self.entryCheck
                                        )
        self.submit_add.grid(row=5,
                             column=0,
                             pady=5
                             )
        self.eyes_close = ctk.CTkImage(dark_image=Image.open('Pictures/eye.png'),
                                       )
        self.eye_open = ctk.CTkImage(dark_image=Image.open('Pictures/view.png'),
                                     )
        self.eye3 = ctk.CTkButton(self.currentPass,
                                  image=self.eyes_close,
                                  text="",
                                  corner_radius=0,
                                  fg_color='#343638',
                                  border_spacing=0,
                                  border_color='#343638',
                                  width=13,
                                  hover_color='#333434',
                                  border_width=0,
                                  command=self.show0)
        self.eye3.grid(column=0, row=0, sticky='e', padx=10)
        self.eye1 = ctk.CTkButton(self.newPass,
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
        self.eye1.grid(column=0, row=0, sticky='e', padx=10)
        self.eye2 = ctk.CTkButton(self.retype,
                                  image=self.eyes_close,
                                  text="",
                                  corner_radius=0,
                                  fg_color='#343638',
                                  border_spacing=0,
                                  border_color='#343638',
                                  width=13,
                                  hover_color='#333434',
                                  border_width=0,
                                  command=self.show2)
        self.eye2.grid(column=0, row=0, sticky='e', padx=10)

    def show0(self):
        if self.currentPass.cget('show') == '*':
            self.eye3.configure(image=self.eye_open)
            self.currentPass.configure(show='')
        else:
            self.eye3.configure(image=self.eyes_close)
            self.currentPass.configure(show='*')

    def show1(self):
        if self.newPass.cget('show') == '*':
            self.eye1.configure(image=self.eye_open)
            self.newPass.configure(show='')
        else:
            self.eye1.configure(image=self.eyes_close)
            self.newPass.configure(show='*')

    def show2(self):
        if self.retype.cget('show') == '*':
            self.eye2.configure(image=self.eye_open)
            self.retype.configure(show='')
        else:
            self.eye2.configure(image=self.eyes_close)
            self.retype.configure(show='*')

    def entryCheck(self):
        if len(self.currentPass.get()) and len(self.newPass.get()) and len(self.retype.get()) != 0:
            if self.newPass.get() == self.retype.get():
                self.conn = pew
                self.c = self.conn.cursor()
                with self.conn:
                    self.c.execute("SELECT password FROM user")
                    keyntot = self.c.fetchone()
                for i in keyntot:
                    self.verify = f"{i}"
                if self.verify == self.currentPass.get():
                    with self.conn:
                        self.c.execute("""UPDATE user SET password = :password""", {
                            'password': self.retype.get()})
                        self.add.destroy()
                else:
                    msg = CTkMessagebox(title="Warning Message!",
                                        message="The password you entered is incorrect. Please try again.",
                                        icon="warning", option_1="Cancel", option_2="Retry")
                    if msg.get() == "Retry":
                        self.currentPass.delete(0, 'end')
                    if msg.get() == "Cancel":
                        return self.add.destroy()
            else:
                CTkMessagebox(title="Error", message="The new password and re-type password field is not the same!!!",
                              icon="cancel")
        elif len(self.currentPass.get()) == 0:
            CTkMessagebox(title="Error", message="The current password field is empty!!!", icon="cancel")
        elif len(self.newPass.get()) == 0:
            CTkMessagebox(title="Error", message="The new password field is empty!!!", icon="cancel")
        elif len(self.retype.get()) == 0:
            CTkMessagebox(title="Error", message="The re-type new password field is empty!!!", icon="cancel")

    def choiceshehe(self):
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
        self.choicess.grid(row=5, column=0,)
        for i in range(0, 1):
            self.choicess.grid_columnconfigure(i, weight=0)
            self.choicess.grid_rowconfigure(i, weight=0)
        self.qna = ctk.CTkButton(self.choicess, text='       Question and answer', anchor='w', border_width=1,
                                        border_color='#3b3c3d', fg_color='#242526',
                                        font=ctk.CTkFont(size=12, weight="bold"), hover_color='#252e33',
                                        command=self.verification)
        self.qna.grid(row=0, column=0, ipadx=59, sticky="w", ipady=8)
        self.verification_btn = ctk.CTkButton(self.choicess, text='       Email verification', anchor='w',
                                              border_width=1, border_color='#3b3c3d', fg_color='#242526',
                                              font=ctk.CTkFont(size=12, weight="bold"), hover_color='#252e33',
                                              command=self.brobro)
        self.verification_btn.grid(row=1, column=0, ipadx=70, sticky="w", ipady=8,)
        self.verification_btn2 = ctk.CTkButton(self.choicess, text='       Cancel', anchor='w',
                                               border_width=1, border_color='#3b3c3d', fg_color='#242526',
                                               font=ctk.CTkFont(size=12, weight="bold"), hover_color='#252e33',
                                               command=lambda: self.adde.destroy())
        self.verification_btn2.grid(row=2, column=0, ipadx=77, sticky="w", ipady=8, )

    def brobro(self):
        self.adde.destroy()
        return bros(self.email)


    def verification(self):
        self.adde.destroy()
        self.add = ctk.CTkToplevel(self)
        self.add.geometry("390x320")
        self.add.title('Verification')
        self.add.resizable(0, 0)
        self.add.grab_set()
        self.add_frame = ctk.CTkFrame(self.add)
        self.add_frame.grid(row=5, column=0, ipady=25, padx=10, pady=10)
        for i in range(0, 5):
            self.add_frame.grid_columnconfigure(i, weight=0)
            self.add_frame.grid_rowconfigure(i, weight=1)
        self.add_frame.grid_rowconfigure(2, weight=0)
        self.titles = ctk.CTkLabel(self.add_frame,
                                   text="Two-factor authentication",
                                   font=('Arial', 30, 'bold'))
        self.titles.grid(row=0,
                         column=0,
                         pady=10
                         )
        self.description = ctk.CTkLabel(self.add_frame,
                                        text="Answer the questions from your heart"
                                        )
        self.description.grid(row=2,
                              column=0,
                              )
        self.description = ctk.CTkLabel(self.add_frame,
                                        text="Who is your child hood best friend?",
                                        font=('Arial', 20, 'bold')
                                        )
        self.description.grid(row=1,
                              column=0,
                              )
        self.verifyAnswer = ctk.CTkEntry(self.add_frame,
                                         placeholder_text="  Answer",
                                         placeholder_text_color='gray',
                                         )
        self.verifyAnswer.grid(row=3,
                               column=0,
                               ipadx=70,
                               ipady=5,
                               padx=15,
                               pady=5)
        self.retypeAnswer = ctk.CTkEntry(self.add_frame,
                                         placeholder_text="  Re-type answer",
                                         placeholder_text_color='gray',
                                         )
        self.retypeAnswer.grid(row=4,
                               column=0,
                               ipadx=70,
                               ipady=5,
                               padx=15,
                               pady=5)
        self.submit_add = ctk.CTkButton(self.add_frame,
                                        text='  Add Verification',
                                        corner_radius=100,
                                        fg_color='#212121',
                                        hover_color='#1A1A1A',
                                        command=self.userCheck
                                        )
        self.submit_add.grid(row=5,
                             column=0,
                             pady=5
                             )

    def userCheck(self):
        if len(self.verifyAnswer.get()) and len(self.retypeAnswer.get()) != 0:
            if self.verifyAnswer.get() == self.retypeAnswer.get():
                self.conn = pew
                self.c = self.conn.cursor()
                with self.conn:
                    self.c.execute(f"INSERT INTO verify VALUES (:answer)",
                                   {
                                       'answer': self.retypeAnswer.get()
                                   })
                    self.add.destroy()
            else:
                CTkMessagebox(title="Error", message="The answer and re-type answer field is not the same!!!",
                              icon="cancel")
        elif len(self.currentPass.get()) == 0:
            CTkMessagebox(title="Error", message="The answer field is empty!!!", icon="cancel")
        elif len(self.newPass.get()) == 0:
            CTkMessagebox(title="Error", message="The re-type answer field is empty!!!", icon="cancel")

    ##################################################################################################################

    def account_button_event(self):
        self.scrollable_acc = ctk.CTkScrollableFrame(self, width=140, label_text="Accounts")
        self.scrollable_acc.grid(row=1, column=1, columnspan=2, rowspan=2, sticky="nsew")
        for i in range(0, 6):
            self.scrollable_acc.grid_columnconfigure(i, weight=1)
            self.scrollable_acc.grid_rowconfigure(i, weight=1)
        self.add_file = ctk.CTkButton(self,
                                      text="Add",
                                      width=50,
                                      fg_color='#2b2b2b',
                                      hover_color='#292929',
                                      image=self.plus,
                                      command=self.add_account)
        self.add_file.grid(column=2, row=2, padx=15, ipadx=1)
        self.option_acc_event = ctk.CTkOptionMenu(self.sidebar_frame,
                                                  values=["Add Account", "Sort by Name"],
                                                  command=self.option_acc_event2
                                                  )
        self.option_acc_event.grid(row=7,
                                   column=0,
                                   padx=20,
                                   pady=10)
        self.option_acc_event.set("Select")
        self.entry.bind('<Return>', self.search_accounts)

        # SELECTING FROM ACCOUNT TABLE THE TITLE OF THE ACCOUNTS STORED AND TO BE DISPLAYED IN EVERY BOX IN THE FRAME
        self.c.execute("SELECT oid, acc_name, acc_pass, acc_email FROM accounts")
        self.col = 0
        self.row = 0
        self.index_num = 0
        records = self.c.fetchall()
        for record in records:
            oid = record[0]
            acc_name = record[1]
            acc_pass = record[2]
            acc_email = record[3]
            self.acc = ctk.CTkButton(self.scrollable_acc, text=f"{acc_name}".capitalize(),
                                     fg_color='#214ea7',
                                     hover_color='#3421a7',
                                     command=lambda acc_name=acc_name, password=acc_pass, email=acc_email: self.broom(
                                         acc_name, password, email))
            self.acc.grid(row=self.row, column=self.col, sticky="nsew", padx=5, pady=5, ipady=50)
            self.col += 1
            self.index_num += 1
            if self.col % 6 == 0:
                self.col = 0
                self.row += 1

    def search_accounts(self, event):
        search_term = self.entry.get().strip().lower()  # convert to lowercase

        for widget in self.scrollable_acc.winfo_children():
            widget.destroy()

        self.c.execute("SELECT oid, acc_name, acc_pass, acc_email FROM accounts WHERE acc_name LIKE ?",
                       ('%' + search_term + '%',))
        records = self.c.fetchall()

        # usage of binary search
        index = self.binary_search(records, search_term)

        if index != -1:
            record = records[index]
            oid = record[0]
            acc_name = record[1]
            acc_pass = record[2]
            acc_email = record[3]
            self.acc = ctk.CTkButton(self.scrollable_acc, text=f"{acc_name}".capitalize(),
                                     fg_color='#214ea7',
                                     hover_color='#3421a7',
                                     command=lambda acc_name=acc_name, password=acc_pass, email=acc_email: self.broom(
                                         acc_name, password, email))
            self.acc.grid(row=0, column=0, sticky='ew', padx=5, pady=5, ipady=50)

    def broom(self, name, num, wow):
        self.show_account = ctk.CTkToplevel(self)
        self.show_account.geometry('350x250')
        self.show_account.grab_set()
        self.show_account.title("Account")
        self.show_account.resizable(False, False)
        self.show = ctk.CTkFrame(self.show_account)
        self.show.pack(ipadx=60, ipady=40, padx=10, pady=10)
        self.name = ctk.CTkLabel(self.show, text=f"{name}".capitalize(), font=("New Times Roman", 30))
        self.name.pack(pady=(10, 0))
        self.show_label = ctk.CTkLabel(self.show, text=f"Email:  {wow}",
                                       font=('New times roman', 20), anchor='s')
        self.show_label.pack(
            ipadx=70,
            ipady=5,
            padx=10,
            pady=5)
        self.password = ctk.CTkLabel(self.show, text=f"Password:  {num}", font=("New Times Roman", 20), anchor='s')
        self.password.pack(
            padx=10,
            pady=(3, 0))
        self.edit_button = ctk.CTkButton(self.show, text="Edit", command=lambda: self.edit_account(name, num, wow))
        self.edit_button.pack(side='top', fill='x', pady=(10, 0))
        self.delete_button = ctk.CTkButton(self.show, text="Delete", command=lambda: self.delete_account(name))
        self.delete_button.pack(side='top', fill='x', pady=(10, 0))

    def delete_account(self, name):
        if not name:
            CTkMessagebox(title="Error", message="Account name not provided!", icon="cancel")
            return
        self.conn = pew
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM accounts WHERE acc_name = :title", {'title': name})
        existing_note = self.c.fetchone()

        if existing_note:
            with self.conn:
                self.c.execute("DELETE FROM accounts WHERE acc_name = :title", {'title': name})
            self.conn.commit()
            self.account_button_event()
            self.show_account.destroy()
        else:
            CTkMessagebox(title="Error", message="Note not found!", icon="cancel")

    def edit_account(self, old_name, old_pass, old_email):
        self.show_account.destroy()
        self.account_edit = ctk.CTkToplevel(self)
        self.account_edit.geometry("400x300")
        self.account_edit.title("Edit Account Information")
        self.account_edit.grab_set()

        self.account_editframe = ctk.CTkFrame(self.account_edit)
        self.account_edit.resizable(False, False)
        self.account_editframe.pack(ipadx=90, ipady=45, padx=10, pady=10)

        self.edit_label = ctk.CTkLabel(self.account_editframe,
                                       text="EDIT USER",
                                       font=('Arial', 30, 'bold'))
        self.edit_label.grid(row=0,
                             column=0,
                             ipadx=70,
                             ipady=5,
                             padx=(15, 10),
                             pady=(10, 0))
        self.title_edit = ctk.CTkEntry(self.account_editframe,
                                       placeholder_text="  Account on",
                                       placeholder_text_color='gray')
        self.title_edit.grid(row=1,
                             column=0,
                             ipadx=70,
                             ipady=5,
                             padx=(15, 10),
                             pady=10)
        self.email_edit = ctk.CTkEntry(self.account_editframe,
                                       placeholder_text="  New Email",
                                       placeholder_text_color='gray')
        self.email_edit.grid(row=2,
                             column=0,
                             ipadx=70,
                             ipady=5,
                             padx=(15, 10),
                             pady=(0, 10))
        self.pass_edit = ctk.CTkEntry(self.account_editframe,
                                      placeholder_text="  New Password",
                                      placeholder_text_color='gray', show='*')
        self.pass_edit.grid(row=3,
                            column=0,
                            ipadx=70,
                            ipady=5,
                            padx=(15, 10),
                            pady=(0, 10))
        self.show_button1 = ctk.CTkSwitch(self.account_editframe,
                                          text="Show password",
                                          command=self.show4)
        self.show_button1.place(x=65,
                                y=210)
        self.submit_edit = ctk.CTkButton(self.account_editframe,
                                         text='Apply Changes',
                                         corner_radius=100,
                                         fg_color='#0b7bff',
                                         hover_color='#4652ff',
                                         command=lambda: self.update_account(old_email, self.pass_edit.get(),
                                                                             self.title_edit.get(),
                                                                             self.email_edit.get()))
        self.submit_edit.place(x=120,
                               y=240)

    def update_account(self, old_email, new_pass, new_name, new_email):
        self.c.execute("UPDATE accounts SET acc_pass=?, acc_name=?, acc_email=? WHERE acc_email=?",
                       (new_pass, new_name, new_email, old_email))
        self.conn.commit()
        self.account_button_event()
        self.account_edit.destroy()

    def add_account(self):
        self.account_add = ctk.CTkToplevel(self)
        self.account_add.geometry("400x300")
        self.account_add.title("Create User")
        self.account_add.grab_set()
        self.account_frame = ctk.CTkFrame(self.account_add)
        self.account_add.resizable(False, False)
        self.account_frame.pack(ipadx=90, ipady=45, padx=10, pady=10)

        self.add_label = ctk.CTkLabel(self.account_frame,
                                      text="CREATE USER",
                                      font=('Arial', 30, 'bold'))
        self.add_label.grid(row=0,
                            column=0,
                            ipadx=70,
                            ipady=5,
                            padx=(15, 10),
                            pady=(10, 0))
        self.title_add = ctk.CTkEntry(self.account_frame,
                                      placeholder_text="  Account on",
                                      placeholder_text_color='gray')
        self.title_add.grid(row=1,
                            column=0,
                            ipadx=70,
                            ipady=5,
                            padx=(15, 10),
                            pady=10)
        self.email_add = ctk.CTkEntry(self.account_frame,
                                      placeholder_text="  Email",
                                      placeholder_text_color='gray')
        self.email_add.grid(row=2,
                            column=0,
                            ipadx=70,
                            ipady=5,
                            padx=(15, 10),
                            pady=(0, 10))
        self.pass_add = ctk.CTkEntry(self.account_frame,
                                     placeholder_text="  Password",
                                     placeholder_text_color='gray', show='*')
        self.pass_add.grid(row=3,
                           column=0,
                           ipadx=70,
                           ipady=5,
                           padx=(15, 10),
                           pady=(0, 10))
        self.show_button1 = ctk.CTkSwitch(self.account_frame,
                                          text="Show password",
                                          command=self.show3)
        self.show_button1.place(x=65,
                                y=210)
        self.submit_add = ctk.CTkButton(self.account_frame,
                                        text='Add account',
                                        corner_radius=100,
                                        fg_color='#0b7bff',
                                        hover_color='#4652ff',
                                        command=lambda: self.checker())
        self.submit_add.place(x=120,
                              y=240)

    def checker(self):
        if len(self.pass_add.get()) and len(self.email_add.get()) and len(self.title_add.get()) != 0:
            self.conn = pew
            self.c = self.conn.cursor()
            with self.conn:
                self.c.execute(
                    "INSERT INTO accounts (acc_email, acc_pass, acc_name) VALUES (:email, :password, :name)",
                    {
                        'email': self.email_add.get(),
                        'password': self.pass_add.get(),
                        'name': self.title_add.get()})
            self.account_button_event()
            self.account_add.destroy()
        elif len(self.title_add.get()) == 0:
            CTkMessagebox(title="Error", message="The Title field is empty!!!", icon="cancel")
        elif len(self.email_add.get()) == 0:
            CTkMessagebox(title="Error", message="The Email field is empty!!!", icon="cancel")
        elif len(self.pass_add.get()) == 0:
            CTkMessagebox(title="Error", message="The Password field is empty!!!", icon="cancel")

    def option_acc_event2(self, option):
        if option == "Sort by Name":
            self.sort_accs_by_title()
        elif option == "Add Account":
            self.add_account()

    def sort_accs_by_title(self):
        self.conn = pew
        self.c = self.conn.cursor()
        self.c.execute("SELECT oid, acc_name, acc_pass, acc_email FROM accounts")
        records1 = self.c.fetchall()
        accs_list = list(records1)
        self.merge_sort_accs(accs_list)

    def merge_sort_accs(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            self.merge_sort_accs(left_half)
            self.merge_sort_accs(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i][1].lower() < right_half[j][1].lower():
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1
        self.refresh_accs_display(arr)

    def refresh_accs_display(self, records2):
        self.col = 0
        self.row = 0
        self.index_num = 0

        for record in records2:
            oid = record[0]
            acc_name = record[1]
            acc_pass = record[2]
            acc_email = record[3]
            self.acc = ctk.CTkButton(self.scrollable_acc, text=f"{acc_name}".capitalize(),
                                     fg_color='#214ea7',
                                     hover_color='#3421a7',
                                     command=lambda acc_name=acc_name, password=acc_pass, email=acc_email: self.broom(
                                         acc_name, password, email))
            self.acc.grid(row=self.row, column=self.col, sticky='ew', padx=5, pady=5, ipady=50)
            self.col += 1
            self.index_num += 1
            if self.col % 6 == 0:
                self.col = 0
                self.row += 1

    ##################################################################################################################

    ##################################################################################################################

    def notes_button_event(self):
        self.scrollable_notes = ctk.CTkScrollableFrame(self, width=140, label_text="Notes")
        self.scrollable_notes.grid(row=1, column=1, columnspan=2, rowspan=2, sticky="nsew")
        for i in range(0, 6):
            self.scrollable_notes.grid_columnconfigure(i, weight=1)
            self.scrollable_notes.grid_rowconfigure(i, weight=1)
        self.add_file1 = ctk.CTkButton(self,
                                       text="Add",
                                       width=50,
                                       fg_color='#2b2b2b',
                                       hover_color='#292929',
                                       image=self.plus,
                                       command=self.add_notes)
        self.add_file1.grid(column=2, row=2, padx=15, ipadx=1)
        self.c.execute("SELECT title, notes FROM notes")
        self.notes_button = ctk.CTkOptionMenu(self.sidebar_frame,
                                              values=["Add Note", "Sort by Title"],
                                              command=self.option_note_event)
        self.notes_button.grid(row=7,
                               column=0,
                               padx=20,
                               pady=10)
        self.notes_button.set("Notes sort")
        self.entry.bind('<Return>', self.search_notes)
        self.col = 0
        self.row = 0
        self.index_num = 0
        records = self.c.fetchall()
        for record in records:
            title = record[0]
            notes = record[1]
            self.notes = ctk.CTkButton(self.scrollable_notes, text=f"{title}".capitalize(),
                                       fg_color='#214ea7',
                                       hover_color='#3421a7',
                                       command=lambda title=title, notes=notes: self.notes_show(title, notes))
            self.notes.grid(row=self.row, column=self.col, sticky='ew', padx=5, pady=5, ipady=50)
            self.col += 1
            self.index_num += 1
            if self.col % 6 == 0:
                self.col = 0
                self.row += 1

    def search_notes(self, event):
        search_term = self.entry.get().strip().lower()  # convert to lowercase

        for widget in self.scrollable_notes.winfo_children():
            widget.destroy()

        self.c.execute("SELECT oid, title, notes FROM notes WHERE title LIKE ?", ('%' + search_term + '%',))
        records = self.c.fetchall()

        # usage of binary search
        index = self.binary_search(records, search_term)

        if index != -1:
            record = records[index]
            oid = record[0]
            title = record[1]  # Use record[1] for title
            notes = record[2]  # Use record[2] for notes
            self.notes = ctk.CTkButton(self.scrollable_notes, text=f"{title}".capitalize(),
                                       fg_color='#214ea7',
                                       hover_color='#3421a7',
                                       command=lambda title=title, notes=notes: self.notes_show(
                                           title, notes))
            self.notes.grid(row=0, column=0, sticky='ew', padx=5, pady=5, ipady=50)

        else:
            print(f"Note with title '{search_term}' not found.")

    def notes_show(self, name, wow):
        self.show_account = ctk.CTkToplevel(self)
        self.show_account.geometry('500x280')
        self.show_account.grab_set()
        self.show_account.title("Notes")
        self.show_account.resizable(True, False)
        self.show = ctk.CTkFrame(self.show_account)
        self.show.pack(ipadx=60, ipady=40, padx=10, pady=10)
        self.name = ctk.CTkLabel(self.show, text=f"{name}".capitalize(), font=("New Times Roman", 30))
        self.name.pack(pady=(10, 0))
        self.show_label = ctk.CTkLabel(self.show, text=f"Note:  {wow}",
                                       font=('New times roman', 20), anchor='s')
        self.show_label.pack(
            ipadx=220,
            ipady=50,
            padx=10,
            pady=5)
        self.edit_button = ctk.CTkButton(self.show, text="Edit", command=lambda: self.edit_note_window(name, wow))
        self.edit_button.pack(side='top', fill='x', pady=(10, 0))

        # delete button
        self.delete_button = ctk.CTkButton(self.show, text="Delete", command=lambda: self.delete_note(name))
        self.delete_button.pack(side='top', fill='x', pady=(10, 0))

    def add_notes(self):
        self.account_add = ctk.CTkToplevel(self)
        self.account_add.geometry("400x250")
        self.account_add.title("Create Notes")
        self.account_add.grab_set()
        self.account_frame = ctk.CTkFrame(self.account_add)
        self.account_add.resizable(False, False)
        self.account_frame.pack(ipadx=90, ipady=35, padx=10, pady=10)

        self.add_label = ctk.CTkLabel(self.account_frame,
                                      text="CREATE NOTE",
                                      font=('Arial', 30, 'bold'))
        self.add_label.grid(row=0,
                            column=0,
                            ipadx=70,
                            ipady=5,
                            padx=(15, 10),
                            pady=(10, 0))
        self.title_notes_add = ctk.CTkEntry(self.account_frame,
                                            placeholder_text="  Title",
                                            placeholder_text_color='gray')
        self.title_notes_add.grid(row=1,
                                  column=0,
                                  ipadx=70,
                                  ipady=5,
                                  padx=(15, 10),
                                  pady=10)
        self.notes_add = ctk.CTkEntry(self.account_frame,
                                      placeholder_text="  Notes",
                                      placeholder_text_color='gray')
        self.notes_add.grid(row=2,
                            column=0,
                            ipadx=70,
                            ipady=5,
                            padx=(15, 10),
                            pady=(0, 10))
        self.submit_add = ctk.CTkButton(self.account_frame,
                                        text='Add account',
                                        corner_radius=100,
                                        fg_color='#0b7bff',
                                        hover_color='#4652ff',
                                        command=lambda: self.checker_notes())
        self.submit_add.place(x=120,
                              y=170)

    def delete_note(self, name):
        if not name:
            CTkMessagebox(title="Error", message="Note title not provided!", icon="cancel")
            return
        self.conn = pew
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM notes WHERE title = :title", {'title': name})
        existing_note = self.c.fetchone()
        if existing_note:
            with self.conn:
                self.c.execute("DELETE FROM notes WHERE title = :title", {'title': name})
            self.conn.commit()
            self.notes_button_event()
            self.show_account.destroy()
        else:
            CTkMessagebox(title="Error", message="Note not found!", icon="cancel")

    def edit_note_window(self, old_title, old_notes):
        self.show_account.destroy()
        self.edit_window = ctk.CTkToplevel(self)
        self.edit_window.geometry("325x250")
        self.edit_window.title("Edit Note")
        self.edit_window.grab_set()

        self.edit_frame = ctk.CTkFrame(self.edit_window)
        self.edit_window.resizable(False, False)
        self.edit_frame.pack(ipadx=90, ipady=35, padx=10, pady=10)

        self.edit_label = ctk.CTkLabel(self.edit_frame,
                                       text="EDIT NOTE",
                                       font=('Arial', 30, 'bold'))
        self.edit_label.grid(row=0,
                             column=0,
                             ipadx=70,
                             ipady=5,
                             padx=(15, 10),
                             pady=(10, 0))

        self.title_entry = ctk.CTkEntry(self.edit_frame,
                                        placeholder_text="New Title",
                                        placeholder_text_color='gray')
        self.title_entry.grid(row=1,
                              column=0,
                              ipadx=70,
                              ipady=5,
                              padx=(15, 10),
                              pady=10)

        self.notes_entry = ctk.CTkEntry(self.edit_frame,
                                        placeholder_text="New Note",
                                        placeholder_text_color='gray')
        self.notes_entry.grid(row=2,
                              column=0,
                              ipadx=70,
                              ipady=5,
                              padx=(15, 10),
                              pady=(0, 10))

        self.submit_edit = ctk.CTkButton(self.edit_frame,
                                         text='Update Note',
                                         corner_radius=100,
                                         fg_color='#0b7bff',
                                         hover_color='#4652ff',
                                         command=lambda: self.update_note(old_title, self.title_entry.get(),
                                                                          self.notes_entry.get()))
        self.submit_edit.grid(row=3,
                              column=0,
                              columnspan=2,
                              pady=10)

    def update_note(self, old_title, new_title, new_notes):
        # update database to new information
        self.c.execute("UPDATE notes SET title=?, notes=? WHERE title=?", (new_title, new_notes, old_title))
        self.conn.commit()
        self.notes_button_event()
        self.edit_window.destroy()

    def checker_notes(self):
        if len(self.title_notes_add.get()) and len(self.notes_add.get()) != 0:
            self.conn = pew
            self.c = self.conn.cursor()
            with self.conn:
                self.c.execute(
                    "INSERT INTO notes (title, notes) VALUES (:title, :notes)",
                    {
                        'title': self.title_notes_add.get(),
                        'notes': self.notes_add.get()})
            self.notes_button_event()
            self.account_add.destroy()
        elif len(self.title_notes_add.get()) == 0:
            CTkMessagebox(title="Error", message="The Title field is empty!!!", icon="cancel")
        elif len(self.notes_add.get()) == 0:
            CTkMessagebox(title="Error", message="The Notes field is empty!!!", icon="cancel")

    def option_note_event(self, option):
        if option == "Add Note":
            self.add_notes()

        elif option == "Sort by Title":
            self.sort_notes_by_title()

    def sort_notes_by_title(self):
        self.conn = pew
        self.c = self.conn.cursor()
        self.c.execute("SELECT title, notes FROM notes")
        records = self.c.fetchall()
        notes_list = list(records)
        self.merge_sort(notes_list)

    def merge_sort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            self.merge_sort(left_half)
            self.merge_sort(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i][0].lower() < right_half[j][0].lower():
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1
        self.refresh_notes_display(arr)

    def refresh_notes_display(self, sorted_notes):
        self.col = 0
        self.row = 0
        self.index_num = 0

        for record in sorted_notes:
            title1 = record[0]
            notes = record[1]
            self.notes = ctk.CTkButton(self.scrollable_notes, text=f"{title1}".capitalize(),
                                       fg_color='#214ea7',
                                       hover_color='#3421a7',
                                       command=lambda title1=title1, notes=notes: self.notes_show(title1, notes))
            self.notes.grid(row=self.row, column=self.col, sticky='ew', padx=5, pady=5, ipady=50)

            self.col += 1
            self.index_num += 1
            if self.col % 6 == 0:
                self.col = 0
                self.row += 1

    #####################################################################################################################

    #####################################################################################################################

    def pictures_button_event(self):
        self.scrollable_picture = ctk.CTkScrollableFrame(self, width=140, label_text="Pictures")
        self.scrollable_picture.grid(row=1, column=1, columnspan=2, rowspan=2, sticky="nsew")
        for i in range(0, 6):
            self.scrollable_picture.grid_columnconfigure(i, weight=1)
            self.scrollable_picture.grid_rowconfigure(i, weight=1)

        self.add_file3 = ctk.CTkButton(self,
                                       text="Add",
                                       fg_color='#2b2b2b',
                                       width=50,
                                       hover_color='#292929',
                                       border_spacing=0,
                                       image=self.plus,
                                       border_width=0,
                                       command=self.insertandoutput)
        self.add_file3.grid(column=2, row=2, padx=15, ipadx=1)
        self.c.execute("SELECT pictures FROM picture")
        records = self.c.fetchall()
        self.col = 0
        self.row = 0

        for record in records:
            image_data = record[0]
            image = Image.open(io.BytesIO(image_data))
            resized_image = image.resize((125, 110))
            photo = ImageTk.PhotoImage(resized_image)
            self.notes = ctk.CTkButton(self.scrollable_picture, text="", image=photo,
                                       fg_color='#214ea7',
                                       hover_color='#3421a7',
                                       command=lambda picture=image_data: self.picture_show(picture))
            self.notes.grid(row=self.row, column=self.col, padx=5, pady=5,
                            ipady=12, ipadx=12, sticky="nsew")
            self.col += 1
            if self.col % 6 == 0:
                self.col = 0
                self.row += 1

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)

    def picture_show(self, pic):
        self.show_account = ctk.CTkToplevel(self, )
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_height = 500
        window_width = 550
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        self.show_account.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        self.show_account.geometry('480x540')
        self.show_account.grab_set()
        self.show_account.overrideredirect(True)
        self.show = ctk.CTkFrame(self.show_account, corner_radius=20)
        image = Image.open(io.BytesIO(pic))
        resized_image = image.resize((450, 440))
        photo = ImageTk.PhotoImage(resized_image)
        self.show.pack(ipadx=10, ipady=10, padx=10, pady=(10, 5))
        self.name = ctk.CTkLabel(self.show, image=photo, text="", )
        self.name.pack(pady=10)
        self.delete_button = ctk.CTkButton(self.show, text="Delete", command=lambda: self.delete_picture(pic))
        self.delete_button.pack(ipady=7, pady=(0, 5), padx=(0, 80), side='right')
        self.delete_button = ctk.CTkButton(self.show, text="Close", command=lambda: self.show_account.destroy())
        self.delete_button.pack(ipady=7, pady=(0, 5), padx=(80, 0), side='left')

    def delete_picture(self, pic):
        self.c.execute("DELETE FROM picture WHERE pictures = ?", (pic,))
        self.conn.commit()
        self.pictures_button_event()
        self.show_account.destroy()

    ################################################################################################################

    ################################################################################################################

    def filedialogs(self):
        global get_image
        # FILEOPENOPTIONS = dict(defaultextension=".pdf", initialdir="D://workspace",
        #                        filetypes=[('pdf file', '*.pdf')])
        get_image = filedialog.askopenfilenames(title="SELECT IMAGE",
                                                filetypes=(("png", "*.png"),
                                                           ("jpg", "*.jpg"),
                                                           ("Allfile", "*.*")))

    # Image need to be conver into binary before insert into database
    def conver_image_into_binary(self, filename):
        with open(filename, 'rb') as file:
            photo_image = file.read()
        return photo_image

    def insert_image(self):
        self.image_database = pew
        data = self.image_database.cursor()
        with self.image_database:
            for image in get_image:
                insert_photo = self.conver_image_into_binary(image)
                data.execute("INSERT INTO picture (pictures) Values (:image)",
                             {'image': insert_photo})
    def insertandoutput(self):
        self.filedialogs()
        self.insert_image()
        self.pictures_button_event()


    def show3(self):
        if self.pass_add.cget('show') == '*':
            self.pass_add.configure(show='')
        else:
            self.pass_add.configure(show='*')

    def show4(self):
        if self.pass_edit.cget('show') == '*':
            self.pass_edit.configure(show='')
        else:
            self.pass_edit.configure(show='*')

    def binary_search(self, records, search_term):
        left, right = 0, len(records) - 1

        while left <= right:
            mid = (left + right) // 2
            current_name = records[mid][1].lower()  # convert to lowercase

            if current_name.startswith(search_term.lower()):
                return mid
            elif current_name < search_term.lower():
                left = mid + 1
            else:
                right = mid - 1

        for i in range(len(records)):
            if records[i][1].lower().startswith(search_term.lower()):
                return i

        return -1
