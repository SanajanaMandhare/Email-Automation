import pandas as pd
import smtplib

SenderAddress = "pythonproject706@gmail.com"
password = "python@21"

e = pd.read_excel("email.xlsx")
emails = e['Emails'].values
names = e["Names"].values
print(f"The receiver's mail ids are : \n\n{emails}")

server = smtplib.SMTP("smtp.gmail.com", 587, timeout=15)
server.starttls()
server.login(SenderAddress, password)

for email,name in zip(emails,names):
	subject = "Hello world - dynamic"
	msg = f"Hello {name};\n\n\nThis is an email from python"
	body = "Subject: {}\n\n{}".format(subject,msg)
	server.sendmail(SenderAddress, email, body)

print("\n\nAll emails have been sent successfully...!")
server.quit()