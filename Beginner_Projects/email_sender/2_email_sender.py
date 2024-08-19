"""
Go over to our gmail account and setup 2 factor authentication
generate app password
create function to send the email
"""

from email.message import EmailMessage
from app2 import password
import ssl
import smtplib

email_sender = 'panorama.spectrum@gmail.com'
email_password = password
email_recceiver = 'malinga.hasantha@gmail.com'
subject = "Don't forget to subscribe"
body = """
When you watch the video, please hit subscribe.
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_recceiver
em['subject'] = subject
em.set_content(body)

context_ = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context_) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_recceiver, em.as_string())