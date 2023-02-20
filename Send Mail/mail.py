# import the smtplib module. It should be included in Python by default
import smtplib
import time

server = smtplib.SMTP('smtp.office365.com', port=587) # smtp-mail.outlook.com
server.starttls()
server.login("amrit.adb@outlook.com", "Sydnry#987")
print ('server working fine')

sender = "amrit.adb@outlook.com"
receivers = ["amrit.referral@gmail.com"]
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