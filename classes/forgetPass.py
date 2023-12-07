import os
from CTkMessagebox.ctkmessagebox import CTkMessagebox
import customtkinter as ctk

from classes.emailCoding import rere
from resetPass import resets


class forget(ctk.CTkToplevel):
    def __init__(self, number):
        super().__init__()
        window_height = 400
        window_width = 550
        self.overrideredirect(True)
        self.resizable(0, 0)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        self.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        self.acc_frame = None
        self.title('THE VAULT')
        self.geometry("470x360")
        self.grab_set()
        self.add_frame = ctk.CTkFrame(self, fg_color='#202020', corner_radius=20)
        self.add_frame.pack(ipadx=100, ipady=100)
        self.titles = ctk.CTkLabel(self.add_frame,
                                   text="Find your account",
                                   font=('Arial', 30, 'bold'))
        self.titles.pack(anchor='w', pady=(60, 15), padx=20)
        self.separator = ctk.CTkLabel(self.add_frame, text="───────────────────────────────────",
                                      text_color='black'
                                      )
        self.separator.pack()
        self.titles = ctk.CTkLabel(self.add_frame,
                                   text="Please enter your email or \n mobile number to search for your account.",
                                   font=('Arial', 11, 'bold'))
        self.titles.pack(pady=10)
        self.searchAcc = ctk.CTkEntry(self.add_frame,
                                      placeholder_text="  Username",
                                      placeholder_text_color='gray',
                                      border_color = '#303030'
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
                                    command=lambda: self.searchAcc1(number)
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

    def searchAcc1(self, number):
        if number == 1:
            if len(self.searchAcc.get()) != 0:
                self.check_check = f'{self.searchAcc.get()}.db'
                self.state = os.path.exists(self.check_check)
                if self.state is True:
                    resets(self.searchAcc.get())
                    return forget.destroy(self)
                else:
                    msg = CTkMessagebox(title="Warning Message!", message="Coundn't find your Account!",
                                        icon="warning", option_1="Cancel", option_2="Retry")
                    if msg.get() == "Retry":
                        self.searchAcc.delete(0, 'end')
                    if msg.get() == "Cancel":
                        return forget.destroy(self)

            else:
                CTkMessagebox(title="Error", message="The search field is empty!!!",
                              icon="cancel")
        elif number == 2:
            if len(self.searchAcc.get()) != 0:
                self.check_check = f'{self.searchAcc.get()}.db'
                self.state = os.path.exists(self.check_check)
                if self.state is True:
                    rere(self.searchAcc.get())
                    return forget.destroy(self)
                else:
                    msg = CTkMessagebox(title="Warning Message!", message="Coundn't find your Account!",
                                        icon="warning", option_1="Cancel", option_2="Retry")
                    if msg.get() == "Retry":
                        self.searchAcc.delete(0, 'end')
                    if msg.get() == "Cancel":
                        return forget.destroy(self)

            else:
                CTkMessagebox(title="Error", message="The search field is empty!!!",
                              icon="cancel")