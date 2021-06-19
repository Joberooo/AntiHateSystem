import smtplib
import string
from email.message import EmailMessage
from email.charset import Charset


class EmailSender:
    def __init__(self, system_email: string, system_pass: string, user_mail: string) -> None:

        self.__set_recv(user_mail)
        self.smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        self.smtpObj.login(system_email, system_pass)
        self.sender = system_email

    def send_notification(self, subject="#HejtAlert!") -> None:
        if not self.receivers: raise Exception("Lack of receivers!")

        try:
            with open('../antihate/analysis_task/alert_content.html', 'r', encoding='UTF-8') as file:
                content = file.read()

            for receiver in self.receivers:
                msg = EmailMessage()
                msg['Subject'] = subject
                msg['From'] = self.sender
                msg['To'] = receiver

                msg.set_content(content, subtype='html', charset='UTF-8')
                msg.set_charset(Charset('UTF-8'))

                self.smtpObj.send_message(msg)

                print("Successfully sent email to:", *self.receivers)
        except smtplib.SMTPException:
            print("Error: unable to send email")

    def __clr_recv(self) -> None:
        self.receivers.clear()

    def __set_recv(self, receivers) -> None:
        if isinstance(receivers, str): receivers = [receivers]
        if not isinstance(receivers, list): raise Exception("Unsupported receivers type!")

        self.receivers = receivers

    def __add_recv(self, receivers) -> None:
        if isinstance(receivers, str):
            self.receivers.append(receivers)
        elif isinstance(receivers, list):
            self.receivers += receivers
        else:
            raise Exception("Unsupported receivers type!")

    def __fin(self) -> None:
        self.smtpObj.close()
