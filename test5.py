import smtplib
from email.message import EmailMessage
import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server_login_mail = "pythonproject706@gmail.com"
server_login_password = "python@21"
server.login(server_login_mail, server_login_password)


def say(text):
    engine.say(text)
    engine.runAndWait()


say("hello sir, how can i help you? myself email assistant")


def assistant_listener():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            info = listener.recognize_google(voice, language="en-in").lower()
            return info

    except:
        return "no"


def send_email(rec, subject, message):
    email = EmailMessage()
    email['From'] = server_login_mail
    email['To'] = rec
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


contact = {
    "name_1": "email_1", #enter name_1 and mail_1
    "name_2": "email_2", #enter name_2 and mail_2
    "name_3": "email_3", #enter name_3 and mail_3
}


def whattodo():
    listen_me = assistant_listener()
    if "assistant" in listen_me:
        if "write mail" in listen_me:
            say("To whom you want to send mail?")
            try:
                user = assistant_listener()
                email = contact[user]
                print(email)
            except:
                say(user+" not found in your contacts!")
                return 0
            say("What is the subject of your email?")
            subject = assistant_listener()
            print(subject)
            say("Tell me the text in your email?")
            message = assistant_listener()
            print(message)
            send_email(email, subject, message)
            say("Email Send Successfully")
            print("Email Send Successfully")

while True:
    whattodo()