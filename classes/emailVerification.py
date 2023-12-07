import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import random
import string


class emailVer:
    def __init__(self):
        self.sender_email = "thevault.noreplyG1@gmail.com"
        self.sender_password = "uxcv fyrx phfa ccec"

    def generate_random_code(self):
        self.characters = string.ascii_letters + string.digits

        # random 8-character code
        self.random_code = ''.join(random.choice(self.characters) for _ in range(8))

        return self.random_code


    def send_email(self, receiver_email, random_code):
        message = MIMEMultipart()
        message["From"] = self.sender_email
        message["To"] = receiver_email
        message["Subject"] = 'The Vault Verification Code'

        message.attach(MIMEText("Your verification code is: " + random_code, "plain"))
        message.attach(MIMEText("\n\nUse the code provided to change your password.", "plain"))

        message.attach(MIMEText("\n\nThis is to help us protect your account.", "plain"))
        message.attach(MIMEText("""\nWe take your online security seriously and are committed to ensuring the safety and privacy of your data. 
This added layer of security will significantly reduce the risk of unauthorized access to your VAULT account
which contains private information.""", "plain"))

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()

            # login to email acc
            server.login(self.sender_email, self.sender_password)

            # send email
            server.sendmail(self.sender_email, receiver_email, message.as_string())

        print("Email sent successfully")
