import pandas as pd
import smtplib
import imghdr
from email.message import EmailMessage

SenderAddress = "pythonproject706@gmail.com"
password = "python@21"

e = pd.read_excel("email.xlsx")
emails = e['Emails'].values
names = e["Names"].values
file = "info.png"
msg = EmailMessage()
msg['Subject'] = "Hello world - dynamic"
msg['From'] = SenderAddress
print(f"The receiver's mail ids are : \n\n{emails}")

with smtplib.SMTP("smtp.gmail.com", 587, timeout=15) as server:
	server.starttls()
	server.login(SenderAddress, password)
	
	with open(file, 'rb') as f:
		file_data = f.read()
		file_type = imghdr.what(f.name)
		file_name = f.name

	for email,name in zip(emails,names):
		
		msg['To'] = email
		
		body = f"Hello {name};\n\n\nThis is an email from python"
		# msg = "Subject: {}\n\n{}".format(subject,body)
		msg.set_content(body)
		msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)
		server.send_message(msg)
		# server.sendmail(SenderAddress, email, msg)
	server.quit()
	del msg['To']
	print('Mail Sent')
