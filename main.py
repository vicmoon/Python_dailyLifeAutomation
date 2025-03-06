# Every Sunday morning send a reminder email 
import smtplib
from datetime import date
import my_creds  # Import credentials

# Load credentials
MY_EMAIL = my_creds.my_email
PASSWORD = my_creds.password

# Check if today is Sunday (6 represents Sunday)
sunday = date.today().weekday() == 6  

def get_recipients(filename="recipients.txt"):
    try:
        with open(filename, "r") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print("Recipients file not found")
        return []

# Load recipients
recipients = get_recipients()

# Check if it's Sunday and we have recipients
if sunday and recipients:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # Secure the connection
        connection.login(user=MY_EMAIL, password=PASSWORD)  # Use correct credentials

        # Email message
        text = "Duty is calling! It's time to add the money!"

        for recipient in recipients:
            connection.sendmail(
                from_addr=MY_EMAIL, 
                to_addrs=recipient,
                msg=f"Subject: TEST!! Reminder  :) \n\n{text}"
            )
    print("Emails sent successfully!")
else:
    print("It's not Sunday or no recipients found")
