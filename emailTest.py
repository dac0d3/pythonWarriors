
from email.message import EmailMessage
import ssl 
import smtplib

sender = 'pythonparlorcomp380@gmail.com'
password = 'qtla xnli ocey umsq' # pythonWarriors1013@LOL

receiver = 'diego_carbajal3@icloud.com'

subject = 'Python Parlor recent order'


body = """
Python Parlor Confirmation

"""




em = EmailMessage()
em['From'] = sender
em['To'] = receiver
em['subject'] = subject

em.set_content(body)


context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context = context) as smtp:
    smtp.login(sender,password)
    smtp.sendmail(sender,receiver,em.as_string())