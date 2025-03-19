import requests
import smtplib
import time

AUTOMATIC_MAIL_ADRESS = "ABC"
AUTOMATIC_MAIL_PASSWORD = '***'
MAIL_RECIPIENT = "XYZ"

endpoint = "https://api.openweathermap.org/data/2.5/forecast"
params={
    "appid": "xyz123",
    "lat": 0,
    "lon": 0,
    "cnt": 4,
}

response = requests.get(endpoint,params=params)
response.raise_for_status()

while True:
    for each_check in response.json()["list"]:
        weather_id = each_check["weather"][0]["id"]
        if weather_id<700:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=AUTOMATIC_MAIL_ADRESS, password=AUTOMATIC_MAIL_PASSWORD)
                connection.sendmail(from_addr=AUTOMATIC_MAIL_ADRESS, to_addrs=MAIL_RECIPIENT,
                                    msg=f"Subject:Weather alert!\n\n Take an umbrela")
            break
        else:
            print("Check again")
    time.sleep(7200)


