import requests
from bs4 import BeautifulSoup

selected_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")
# selected_date = "1996-10-21"

header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:138.0) Gecko/20100101 Firefox/138.0"}

URL = f"https://www.billboard.com/charts/hot-100/{selected_date}"

response = requests.get(URL,headers=header)
data = response.text
soup = BeautifulSoup(data, 'html.parser')
titles = soup.select("li ul li h3")

with open("songs.txt", mode="w", encoding="utf-8") as file:
    for title in titles:
        song_title = title.get_text(strip=True)
        file.write(song_title+"\n")

