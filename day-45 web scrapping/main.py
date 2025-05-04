import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
data = response.text
soup = BeautifulSoup(data, 'html.parser')

titles = soup.find_all("h3", class_="title")
titles = titles[::-1]

with open("movies.txt",mode="w",encoding="utf-8") as file:
    for title in titles:
        print(title.getText())
        file.write(title.getText()+"\n")

