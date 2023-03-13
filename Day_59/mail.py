from smtplib import SMTP


class Mail():
    
    def __init__(self, user="adambayraktar@gmail.com"):
        self.user = user
        # self.password = here enter your password
    
    def send_email(self, info: dict ):
        """
        info: Dict
        Convert dict into message and sends email to self
        """
        body_message = ""
        for key,value in info.items():
            body_message += f"{key}: {value}\n"
        message = f"Subject: Question - Blog\n\n {body_message}"

        with SMTP("smtp.gmail.com", port=587) as smtp:
            smtp.starttls()
            smtp.login(self.user, self.password)
            smtp.sendmail(self.user, self.user, message)