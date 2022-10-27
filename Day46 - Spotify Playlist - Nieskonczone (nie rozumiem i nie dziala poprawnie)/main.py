from bs4 import BeautifulSoup
import requests
# Moduly do obslugi spotify
import spotipy
from spotipy.oauth2 import SpotifyOAuth

music_date = input("Which year do you want to travel to? Type date in this format YYYY-MM-DD:")

URL = f"https://www.billboard.com/charts/hot-100/{music_date}/"
response = requests.get(URL)
website_data = response.text

soup = BeautifulSoup(website_data, "html.parser")

# Najwyrazniej nie trzeba podawac calej nazwy klasy tylko pewien blok z klasy i tez dziala / moze tez byc tak soup.select(selector="div ul li ul li h3") / przy span wyskakuja dodatkowo jakies liczby
best_song_titles = soup.find_all(name="h3", class_="a-no-trucate")
creators = soup.find_all(name="span", class_="a-no-trucate")

# Strip usuwa spacje na poczatku i koncu tekstu
titles_list = [title.getText().strip() for title in best_song_titles]
creators_list = [creator.getText().strip() for creator in creators]


spotify = spotipy.Spotify(
    auth_manager = SpotifyOAuth(
        scope="playlist-modify-private",
        client_id="user id",
        client_secret="secret",
        redirect_uri="http://example.com",
        cache_path="token.txt"
    )
)

user_id = spotify.current_user()["id"]
