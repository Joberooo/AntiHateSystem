from email_sender import EmailSender
from email.message import EmailMessage
import smtplib

from settings.settings import get_parm

if __name__ == "__main__":
    EMAIL_ADDRESS = get_parm("server_email")
    EMAIL_PASSWORD = get_parm("server_pass")
    USER_MAIL = get_parm("receive_email")





    msg = EmailMessage()
    msg['Subject'] = 'Here is my newsletter'
    msg['From'] = get_parm("server_email")
    msg['To'] = get_parm("receive_email")
    msg.set_content('''
    <!DOCTYPE html>
    <html> 
        <body>
            <div style="background-color:#eee;padding:10px 20px;">
                <h2 style="font-family:Georgia, 'Times New Roman', Times, serif;color#454349;">My newsletter</h2>
            </div>
            <div style="padding:20px 0px">
                <div style="height: 500px;width:400px">
                    <img src="https://dummyimage.com/500x300/000/fff&text=Dummy+image" style="height: 300px;">
                    <div style="text-align:center;">z
                        <h3>Article 1</h3>
                        <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. A ducimus deleniti nemo quibusdam iste sint!</p>
                        <a href="#">Read more</a>
                    </div>
                </div>
            </div>
        </body>
    </html>
    ''', subtype='html')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

    # es = EmailSender()
    # es.try_send("hihihihi", msg)