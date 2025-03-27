import requests
from win32ctypes.pywin32.pywintypes import datetime

USERNAME = "***"
TOKEN ="***"
GRAPH_ID = "***"
GRAPH_NAME = "Habit Tracker"
UNIT = "kilogram"
TYPE = "int"
COLOR = "sora"

DATE = datetime.today().strftime("20"'%y%m%d')

params={
    "username" : USERNAME,
    "id" : GRAPH_ID,
    "name" : GRAPH_NAME,
    "unit" : UNIT,
    "type" : TYPE,
    "color": COLOR,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
    "date":DATE,
    "quantity":"1"
}

headers ={
    "X-USER-TOKEN" : TOKEN,
}

endpoint="https://pixe.la/v1/users"

pixel_endpoint = f"{endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
test=requests.post(url=pixel_endpoint,json=params,headers=headers)

print(test.text)
