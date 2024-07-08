# from msilib.schema import MIME
from cryptography.fernet import Fernet
import smtplib, ssl
import settings, secure


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# if there is an error with login (Username and password not accepted), go to 'myaccount.google.com/lesssecureapps' and turn the settings 'on'


def send(sender, receiver, subject, content):
    
    port = 465 # for ssl
    #port = 587
    smtp_server = settings.smtp_server
    #sender_email = settings.sender_email
    #receiver_email = settings.receiver_email
    #sender_email = sender
    #receiver_email = receiver

    port = settings.ssl_port
    password = secure.decrypt(settings.password).decode()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        
        try:

            message = MIMEMultipart('alternative')
            message['Subject'] = subject
            message['From'] = sender
            message['To'] = receiver

            message.attach(MIMEText(content,'html'))

            server.login(sender,password)
            print('successful login')
            res = server.sendmail(sender, receiver, message.as_string())
            print('email sent')
        except:
            print('could not login or send email', res)
