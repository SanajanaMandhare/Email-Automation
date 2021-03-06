import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd 

mail_content = '''Hello {},
This is a test mail.
In this mail we are sending some attachments.
The mail is sent using Python SMTP library.
Thank You!
'''
#The mail addresses and password
sender_address = "pythonproject706@gmail.com"
sender_pass = "python@21"

e = pd.read_excel("email.xlsx")
emails = e['Emails'].values
names = e["Names"].values
print(f"The receiver's mail ids are : \n\n{emails}")

session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password


for email,name in zip(emails,names):
	#Setup the MIME
	message = MIMEMultipart()
	message['From'] = sender_address
	message['To'] = email
	message['Subject'] = 'A test mail sent by Python. It has an attachment.'
	
	message.attach(MIMEText(mail_content.format(name), 'plain'))
	attach_file_name = 'covid.pdf'
	attach_file = open(attach_file_name, 'rb') 
	payload = MIMEBase('application', 'octate-stream')
	payload.set_payload((attach_file).read())
	encoders.encode_base64(payload)
	
	payload.add_header('Content-Decomposition', "attachment", maintype='image', filename= "attach_file_name")
	message.attach(payload)
	text = message.as_string()
	session.sendmail(sender_address, email, text)
session.quit()
print('Mail Sent')