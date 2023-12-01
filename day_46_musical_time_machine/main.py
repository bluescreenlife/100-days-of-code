import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime

# --------- Spotify API & Auth Setup --------- #

load_dotenv()
SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")
SPOTIFY_USERNAME = os.getenv("SPOTIFY_USERNAME")

scope = "playlist-modify-private"
sp_oauth = SpotifyOAuth(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI, scope=scope, cache_path="./token.txt", username=SPOTIFY_USERNAME)
sp = spotipy.Spotify(auth_manager=sp_oauth)
# access_token = sp_oauth.get_access_token() # run once to get token

# ---------- Scrape Billboard Site ---------- #

# user input date         
date = input("Welcome to the Musical Time Machine. I will create a Spotify playlist\n"
              "containing the top songs from any date. Enter a date (YYYY-MM-DD): \n")

# scrape Billboard site for top 100 songs from date
billboard_url = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(billboard_url)
html = response.text

soup = BeautifulSoup(html, "html.parser")
track_divs = soup.find_all("div", class_="o-chart-results-list-row-container")

top_100_songs = []
top_100_artists = []

# create list of top 100 songs
for div in track_divs:
    div_song = div.find("h3", id="title-of-a-story").get_text().strip()
    top_100_songs.append(div_song)
    div_artist = div.select_one("li ul li span").get_text().strip()
    top_100_artists.append(div_artist)

# ---------- Get Spotify Data ---------- #

# get track URIs from Spotify
top_100_songs_uris = []

for song in top_100_songs:
    song_index = top_100_songs.index(song)
    artist = top_100_artists[song_index]

    track_data = sp.search(f"track: {song} artist: {artist} year: {date[:4]}")
    try:
        track_uri = track_data["tracks"]["items"][0]["uri"]
        top_100_songs_uris.append(track_uri)
        print(f"✅ Match found: {song} - {artist}.")
    except IndexError:
        print(f"❌ Song: {song} - {artist} not found in Spotify catalog. Song will not be added to playlist.")

# ---------- Make Date Prettier ---------- #

# convert date input string to datetime object
input_date = datetime.strptime(date, "%Y-%m-%d")

# format datetime object as a text string
output_date_str = input_date.strftime("%B %d, %Y").replace(" 0", " ")

# add suffix

def format_date(input_date_str):
    # Convert the input string to a datetime object
    input_date = datetime.strptime(input_date_str, "%Y-%m-%d")

    # Format the datetime object as a string in the desired format
    formatted_date = input_date.strftime("%B %d, %Y")

    return formatted_date

pretty_date = format_date(date)

# ---------- Create Spotify Playlist ---------- #
user = sp.current_user()["id"]
playlist = sp.user_playlist_create(user=user, name=f"Top 100: {pretty_date}", public=False, collaborative=False, 
                                   description=f"Billboard's top 100 songs from {pretty_date}.")
sp.user_playlist_add_tracks(user=user, playlist_id=playlist["uri"], tracks=top_100_songs_uris)
print(f"🎧 Spotify playlist created: Top 100: {pretty_date}. Happy listening!")