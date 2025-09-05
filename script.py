import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv
import csv
from datetime import datetime

def main():
   

    today = datetime.today()
    today_month_day = (today.month, today.day)
    today_month_day_string = str(today_month_day[0]) + '-' + str(today_month_day[1])
    birthday_person = False

    load_dotenv()

    with open(f'{os.getenv('CSV_PATH')}', mode ='r')as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
            if lines[1] == today_month_day_string:
                birthday_person = lines[0]
            
    if birthday_person:
    
        EMAIL_ADDRESS = f'{os.getenv('EMAIL')}'
        EMAIL_PASSWORD = f'{os.getenv('PASSWORD')}'

        msg = EmailMessage()
        msg['Subject'] = 'Birthday Alert!'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = EMAIL_ADDRESS
        msg.set_content(f"Hello Caleb! Here is a reminder that it is {birthday_person}'s birthday!")

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)

if __name__ == "__main__":
    main()