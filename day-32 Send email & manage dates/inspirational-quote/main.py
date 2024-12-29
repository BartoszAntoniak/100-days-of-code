import smtplib
import datetime as dt
import random

my_email = "XYZ"
password = "*****"

now = dt.datetime.now()
current_weekday = now.weekday()

if current_weekday==6:
    with open("quotes.txt") as quote_file:
        all_quotes=quote_file.readlines()
        quote = random.choice(all_quotes)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs="ZXY",msg=f"Subject:TEST\n\n{quote}")
