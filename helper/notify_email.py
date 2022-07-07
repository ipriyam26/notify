import smtplib
from email.message import EmailMessage
from env import *

class NotifyEmail:   
   def __init__(self):
         pass
      
   def send_mail(self,to,body,subject):
      with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
         smtp.login(NOTIFIER_EMAIL,PASSWORD)
         smtp.send_message(self.make_message(to,subject,body))      

   def make_message(self,to, subject, body):
      msg = EmailMessage()
      msg['Subject'] = subject
      msg['From'] = NOTIFIER_EMAIL
      msg['To'] = to
      msg.set_content(body)
      return msg
