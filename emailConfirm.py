
from email.message import EmailMessage
import ssl 
import smtplib


#email1 = 'diego_carbajal3@icloud.com'



# This method sends an email to the customer to confirm their order at python parlor 

def emailConf(email):
    
    sender = 'pythonparlorcomp380@gmail.com'
    password = 'qtla xnli ocey umsq' # pythonWarriors1013@LOL

    receiver = str(email)

    subject = 'Python Parlor Order Confirmation'


    body = """
    You are receiving this email to confirm your order at Python Parlor.  

    Thank you, please come again!

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
        
    print('Email Sent')
        
        
#emailConf(email1)