import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL_ADDRESS = f'{os.getenv('EMAIL')}'
EMAIL_PASSWORD = f'{os.getenv('PASSWORD')}'

msg = EmailMessage()
msg['Subject'] = 'Birthday Alert!'
msg['From'] = EMAIL_ADDRESS
msg['To'] = EMAIL_ADDRESS
msg.set_content('Hello Caleb! This is a test')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)