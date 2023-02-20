# import the smtplib module.
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

sender = "amrit.adb@outlook.com"
receiver = ["amrit.referral@gmail.com"] # should be a list

# Create a multipart message and set headers
msg = MIMEMultipart()
msg["From"] = sender
msg["To"] = ", ".join(receiver)
msg["Subject"] = "SMTP e-mail Test"
body = "This is an automated message being sent by Python. Python is the mastermind behind    this."
msg.attach(MIMEText(body, 'plain')) #msg.attach(MIMEText(html, "html"))

filename = ["1.jpg", "2.jpg"]  # In same directory as script

for file in filename:
    # Open PDF file in binary mode
    with open(file, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        "attachment; filename= %s"%file,
    )

    # Add attachment to message and convert message to string
    msg.attach(part)


# Log in to server using secure context and send email
server = smtplib.SMTP("smtp.office365.com", 587) # smtp-mail.outlook.com, smtp.gmail.com 
server.starttls()
server.login("amrit.adb@outlook.com", "Sydnry#987")
print ('server working fine')
server.sendmail(sender, receiver, msg.as_string())
print ('sending email to outlook')
server.quit()