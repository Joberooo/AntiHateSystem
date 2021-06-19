from email_sender import EmailSender


from settings.settings import get_parm

if __name__ == "__main__":


    es = EmailSender()
    es.try_send(5)