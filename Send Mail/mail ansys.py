import sys
sys.path.append("D:/_Common")
from cred import mailCred

# import the smtplib module.
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

sender = mailCred['sender'] # Gmail not working
receiver = [mailCred['receiver']] # should be a list
print(sender)
a1 = Model.Analyses[0]
a1files = a1.AnalysisSettings.SolverFilesDirectory
a1solvefiles = a1files + 'solve.out'
a1s = a1.Solution
print(a1solvefiles)
if a1s.ObjectState.ToString() == 'Solved':
    sub = 'Analysis Succeeded'
else:
    sub = 'Analysis Failed!'

# Create a multipart message and set headers
msg = MIMEMultipart()
msg["From"] = sender
msg["To"] = ", ".join(receiver)
msg["Subject"] = sub
body = sub
msg.attach(MIMEText(body, 'plain')) #msg.attach(MIMEText(html, "html"))

filename = [a1solvefiles]  # In same directory as script
print(filename)
for file in filename:
    # Open file in binary mode
    with open(file, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    print(file)
    part.add_header(
        "Content-Disposition",
        "attachment; filename= %s"%(file.rsplit('\\')[-1]),
    )

    # Add attachment to message and convert message to string
    msg.attach(part)


# Log in to server using secure context and send email
server = smtplib.SMTP("smtp.office365.com", 587) # smtp-mail.outlook.com, smtp.gmail.com 
server.starttls()
server.login(mailCred['sender'], mailCred['password'])
print ('server working fine')
server.sendmail(sender, receiver, msg.as_string())
print ('sending email to outlook')
server.quit()