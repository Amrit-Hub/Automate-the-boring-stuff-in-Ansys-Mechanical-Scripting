import sys
sys.path.append("D:/_Common")
from cred import mailCred

# import the smtplib module. It should be included in Python by default
import smtplib
import time

server = smtplib.SMTP('smtp-mail.outlook.com', port=587) # smtp-mail.outlook.com smtp.office365.com

# server.starttls()

server.login(mailCred['sender'], mailCred['password'])
print ('server working fine')

sender = mailCred['sender']
receivers = [mailCred['receiver']]
subject = "SMTP e-mail Test" 
body = "This is an automated message being sent by Python. Python is the mastermind behind    this."
message = """From: %s
To: %s
Subject: %s

%s
"""%(sender, ", ".join(receivers), subject, body)
print(message)
server.sendmail(sender, receivers, message)
print ('sending email to outlook')

server.quit()