import smtplib,ssl

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

def sendMailTo(tomail, sub, content):
    port = 587 
    smtp_server = "smtp.gmail.com"
    me = 'test@test.com'
    you = tomail

    msg = MIMEMultipart('alternative')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = you
    PASSWORD = 'paasss'

    part1 = MIMEText(content, 'html')
    msg.attach(part1)
  
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  
            server.starttls(context=context)
            server.ehlo()  
            server.login(me,PASSWORD)
            server.sendmail(me,you, msg.as_string())
        return 'SUCCESS'
    except Exception as e:
        print('Error! Code: {c}, Message, {m}'.format(c = type(e).__name__, m = str(e)))
        c = type(e).__name__
        return c