import sys
sys.path.append("D:/_Common")  # import username password credentials
from cred import mailCred  # import username password credentials

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

warnings = ['warning 1', 'warning 2', 'warning 3']

msg = smtp.MailMessage()
msg.From = smtp.MailAddress(mailCred['sender'])
msg.To.Add(smtp.MailAddress(mailCred['receiver']))
msg.Subject = "Ansys Mechanical Status Update"

row = ""
for warning in warnings:
    row = row + """
    <tr>
        <td>{}</td>
    </tr>
    """.format(warning)

htmlBody = """
<!DOCTYPE html>
<html>
<head>
<style>
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}
</style>
</head>
<body>
<h2>Service Alert</h2>
<p>Below are the list of warnings.</p>
<table>
    <tr>
        <th>Messages</th>
    </tr>
    %s
</table>
</body>
</html>
"""%(row)
msg.Body = htmlBody
msg.IsBodyHtml = True

files = [a1solvefiles]  # In same directory as script
for file in files:
    attachment = smtp.Attachment(file)
    msg.Attachments.Add(attachment)

# Log in to server and send email
client = smtp.SmtpClient('smtp-mail.outlook.com', 587)
client.EnableSsl = True
client.Credentials = net.NetworkCredential(mailCred['sender'], mailCred['password'])
client.Send(msg)