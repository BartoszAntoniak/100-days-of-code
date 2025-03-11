import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 0.0000
MY_LONG = 0.0000
AUTOMATIC_MAIL_ADRESS = "ABC"
AUTOMATIC_MAIL_PASSWORD = '***'
MAIL_RECIPIENT = "XYZ"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

lat_distance = MY_LAT - iss_latitude
long_distance = MY_LONG - iss_longitude

if -5 < lat_distance <5 and -5 < long_distance < 5:
    print("Visible")
    iss_visible = True
else:
    print("Not visible")
    iss_visible = False


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
current_hour = time_now.hour

if sunset < current_hour and current_hour > sunset:
    print("It's night")
    is_night = True
else:
    print("It's day")
    is_night = False

while True:
    if is_night and iss_visible:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=AUTOMATIC_MAIL_ADRESS, password=AUTOMATIC_MAIL_PASSWORD)
            connection.sendmail(from_addr=AUTOMATIC_MAIL_ADRESS, to_addrs=MAIL_RECIPIENT,
                                msg=f"Subject:ISS STATUS\n\n Teraz widac")
    else:
        print("Checked, but ISS is not here at the moment")
    time.sleep(60)




