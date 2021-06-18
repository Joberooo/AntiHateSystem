import smtplib

from settings.settings import get_parm


class EmailSender:
    SYSTEM_MAIL = get_parm("server_email")
    SYSTEM_PASS = get_parm("server_pass")
    USER_MAIL = get_parm("receive_email")

    def __init__(self, receivers=None, sender="Admin@AntiHateSystem.com") -> None:

        self.__set_recv(self.USER_MAIL)
        self.smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        self.smtpObj.login(self.SYSTEM_MAIL, self.SYSTEM_PASS)
        self.sender = sender

    def try_send(self, subject, message) -> None:
        if not self.receivers: raise Exception("Lack of receivers!")

        try:
            full_message = f"Subject: {subject}\n\n{message}"
            self.smtpObj.sendmail(self.sender, self.receivers, full_message)         
            print("Successfully sent email to:", *self.receivers)
        except smtplib.SMTPException:
            print("Error: unable to send email")
        self.__fin()

    def __clr_recv(self) -> None:
        self.receivers.clear()

    def __set_recv(self, receivers) -> None:
        if isinstance(receivers, str): receivers = [receivers]
        if not isinstance(receivers, list): raise Exception("Unsupported receivers type!")
        
        self.receivers = receivers

    def __add_recv(self, receivers) -> None:
        if isinstance(receivers, str): self.receivers.append(receivers)
        elif isinstance(receivers, list): self.receivers += receivers
        else: raise Exception("Unsupported receivers type!")

    def __fin(self) -> None:
        self.smtpObj.close()




    
