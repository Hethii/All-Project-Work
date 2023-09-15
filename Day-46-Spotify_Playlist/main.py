from bs4 import BeautifulSoup
import requests

CLIENT_ID = ""
CLIENT_SECRET = ""

import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="",
    )
)

user_id = sp.current_user()["id"]
playlist_year = input("What year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get("https://www.billboard.com/charts/hot-100/" + playlist_year)
data = response.text

soup = BeautifulSoup(data, "html.parser")
label = soup.select("li ul li h3")
title = [title_names.getText().strip() for title_names in label]

song_uris = []
year = playlist_year.split("-")[0]
for song in title:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} not found in Spotify. SKipped.")

# print(song_uris)

playlist = sp.user_playlist_create(user=user_id, name=f'{playlist_year} Billboard 100',
                                   public=False, description='I Love You, Ezer')
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)























