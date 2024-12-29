##################### Extra Hard Starting Project ######################
import pandas
import smtplib
import datetime as dt
import random

my_email = "XYZ"
password = "*****"

# 1. Update the birthdays.csv
data = pandas.read_csv("./birthdays.csv")
birthday_dictionary = data.to_dict(orient="records")

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
today_day = now.day
today_month = now.month
for each_birthday in birthday_dictionary:
    if each_birthday["day"] == today_day and each_birthday["month"] == today_month:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

        letter_list = ["letter_1.txt","letter_2.txt","letter_3.txt"]
        selected_letter = random.choice(letter_list)
        with open(f"letter_templates/{selected_letter}") as letter_file:
            letter = letter_file.read()
            name_to_replace = each_birthday["name"]
            personalized_letter = letter.replace("[NAME]", name_to_replace)

# 4. Send the letter generated in step 3 to that person's email address.

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=each_birthday["email"],
                                msg=f"Subject:Happy Birthday!\n\n{personalized_letter}")



