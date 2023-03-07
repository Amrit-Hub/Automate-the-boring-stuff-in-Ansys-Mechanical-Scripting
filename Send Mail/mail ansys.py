import sys
sys.path.append("D:/_Common")
from cred import mailCred

import clr
clr.AddReference('System')
import System.Net as net
import System.Net.Mail as smtp

a1 = Model.Analyses[0]
a1files = a1.AnalysisSettings.SolverFilesDirectory
a1solvefiles = a1files + 'solve.out'
a1s = a1.Solution

if a1s.ObjectState.ToString() == 'Solved':
    sub = 'Analysis Succeeded'
else:
    sub = 'Analysis Failed!'

msg = smtp.MailMessage()
msg.From = smtp.MailAddress(mailCred['sender'])
msg.To.Add(smtp.MailAddress(mailCred['receiver']))
msg.Subject = "c test email"
msg.Body = "This is an automated message"
# msg.CC.Add()
# msg.IsBodyHtml = True

files = [a1solvefiles]  # In same directory as script
for file in files:
    attachment = smtp.Attachment(file)
    msg.Attachments.Add(attachment)

# Log in to server and send email
client = smtp.SmtpClient('smtp-mail.outlook.com', 587)
client.EnableSsl = True
client.Credentials = net.NetworkCredential(mailCred['sender'], mailCred['password'])
client.Send(msg)