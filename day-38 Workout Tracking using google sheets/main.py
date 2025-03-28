import requests
import os
from requests.auth import HTTPBasicAuth
from win32ctypes.pywin32.pywintypes import datetime

APP_ID = os.environ.get("APP_ID", "Key does not exist")
API_KEY = os.environ.get("API_KEY", "Key does not exist")
USERNAME = os.environ.get("USERNAME", "Key does not exist")
PASSWORD = os.environ.get("PASSWORD", "Key does not exist")
TOKEN = os.environ.get("TOKEN", "Key does not exist")
SHEET_ENDPOINT = os.environ.get("SHEET_ENDPOINT", "Key does not exist")

query_input = input("What kind of exercise you did?")

headers = {
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY
}

params={
    "query" : query_input
}

endpoint1 = "https://trackapi.nutritionix.com/v2/natural/exercise"
endpoint2 = SHEET_ENDPOINT

test = requests.post(url=endpoint1,json=params,headers=headers)

Date = datetime.now().strftime("%d-%m-20%y")
Time = datetime.now().strftime("%H:%M:%S")
Exercise = (test.json()["exercises"][0]["name"])
Duration = (test.json()["exercises"][0]["duration_min"])
Calories = (test.json()["exercises"][0]["nf_calories"])

auth = HTTPBasicAuth(username=USERNAME,password=PASSWORD)

params2={
    "arkusz1" : {
        "date" : Date,
        "time" : Time,
        "exercise" : Exercise,
        "duration" : Duration,
        "calories" : Calories
            }
}

headers2 = {
    "authorization": TOKEN
}

auth_request = requests.get(endpoint2,auth=auth)
post_results = requests.post(url=endpoint2,json=params2,headers=headers2)

