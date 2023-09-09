import sys
sys.path.append("D:/_Common")  # import username password credentials
from cred import mailCred  # import username password credentials

import clr
clr.AddReference('System')
import System.Net as net
import System.Net.Mail as smtp
from datetime import datetime

msg = smtp.MailMessage()
msg.From = smtp.MailAddress(mailCred['sender'], 'Ansys Service Alert')
msg.To.Add(smtp.MailAddress(mailCred['receiver']))
msg.Subject = "Test email - {}".format(datetime.now())
msg.Body = 'test body'
# msg.CC.Add()
# msg.IsBodyHtml = True

# msg = smtp.MailMessage(sender, ", ".join(receivers), subject, body)

files = [r"C:\Users\amrit\Documents\VSCode\AnsysMechanical\Send Mail\1.jpg", r"C:\Users\amrit\Documents\VSCode\AnsysMechanical\Send Mail\2.jpg"]

for file in files:
    attachment = smtp.Attachment(file)
    msg.Attachments.Add(attachment)


client = smtp.SmtpClient('smtp-mail.outlook.com', 587) # smtp.gmail.com not working on personal email
client.EnableSsl = True
client.Credentials = net.NetworkCredential(mailCred['sender'], mailCred['password'])
client.Send(msg)
msg.Dispose()
client.Dispose()
