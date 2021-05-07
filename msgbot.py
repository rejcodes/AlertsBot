import smtplib
from email.message import EmailMessage

# helper function to email alert message from bot email account
def email_alert(subject, body, recipient):
    msg = EmailMessage()
    msg.set_content(body)

    # replace user and password with email bot's credentials
    user = 'somebody@gmail.com'
    password = 'password123'

    msg['subject'] = subject
    msg['to'] = recipient
    msg['from'] = user


    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    server.login(user, password)
    server.send_message(msg)

    server.quit()