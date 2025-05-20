import requests
from bs4 import BeautifulSoup
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

selected_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")
UserAgent = os.environ.get("UserAgent", "Key does not exist")

header = {
    "User-Agent": UserAgent
}
URL = f"https://www.billboard.com/charts/hot-100/{selected_date}"
response = requests.get(URL, headers=header)
soup = BeautifulSoup(response.text, 'html.parser')
titles = soup.select("li ul li h3")

title_list = [title.get_text(strip=True) for title in titles]

ClientID = os.environ.get("ClientID", "Key does not exist")
ClientSecret = os.environ.get("ClientSecret", "Key does not exist")
RedirectURI = os.environ.get("RedirectURI", "Key does not exist")

auth_manager = SpotifyOAuth(
    client_id=ClientID,
    client_secret=ClientSecret,
    redirect_uri=RedirectURI,
    scope="playlist-modify-private",
    show_dialog=True,
    cache_path="token.txt"
)

sp = spotipy.Spotify(auth_manager=auth_manager)

user_id = sp.current_user()["id"]
year = selected_date.split("-")[0]
song_uris = []

for title in title_list:
    result = sp.search(q=f"{title} {year}", type="track", limit=1)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{title} doesn't exist in Spotify. Skipped.")

playlist_name = f"{selected_date} Billboard 100"

new_playlist = sp.user_playlist_create(
    user=user_id,
    name=playlist_name,
    public=False
)

playlist_id = new_playlist["id"]

sp.playlist_add_items(
    playlist_id=playlist_id,
    items=song_uris,
    position=None,
)

print("Playlist done")