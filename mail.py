from cryptography.fernet import Fernet
import smtplib, ssl
import settings, secure


# if there is an error with login (Username and password not accepted), go to 'myaccount.google.com/lesssecureapps' and turn the settings 'on'


def send(message):
    #port = 465 # for ssl
    #port = 587
    smtp_server = settings.smtp_server
    sender_email = settings.sender_email
    receiver_email = settings.receiver_email
    port = settings.ssl_port
    password = secure.decrypt(settings.password).decode()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        
        try:
            server.login(sender_email,password)
            print('successful login')
            res = server.sendmail(sender_email, receiver_email, message)
            print('email sent')
        except:
            print('could not login or send email', res)