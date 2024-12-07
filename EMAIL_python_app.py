#  go over to our gmail account and setup 2 factor aithentaation
#  generate app password
#  create a function to send the mail.
# https://temp-mail.org/
from email.message import EmailMessage
from  extrA_project.app2 import password
import ssl 
import smtplib

email_sender ='jay414181@gmail.com'
email_password = password 
email_receiver ='vecap91266@dixiser.com'
subject = "today i will start devloping project in python help with youtube"
body="""
when you complite project  , next project devloped know 
"""
em=EmailMessage()
em['From'] =email_sender
em['To'] =email_receiver
em['suject'] = subject
em.set_content(body)

context =ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',456,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())