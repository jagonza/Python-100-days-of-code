import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()


def get_billboard_songs(date):
    response = requests.get(f"{os.getenv('BILLBOARD_BASE_URL')}{date}")
    soup = BeautifulSoup(response.text, "html.parser")
    all_songs_spans = soup.find_all(
        name="span", class_="chart-element__information__song")
    all_songs = [song_span.getText() for song_span in all_songs_spans]
    return all_songs


def get_spotipy_connection():
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(scope="playlist-modify-private",
                                  redirect_uri="http://example.com",
                                  client_id=os.getenv("SPOTIFY_CLIENT_ID"),
                                  client_secret=os.getenv(
                                      "SPOTIFY_CLIENT_SECRET"),
                                  show_dialog=True,
                                  cache_path="token.txt"))
    return sp


def get_songs_uris(sp, date, songs):
    song_uris = []
    year = date.split("-")[0]
    for song in songs:
        result = sp.search(q=f"track:{song} year:{year}", type="track")
        try:
            uri = result["tracks"]["items"][0]["uri"]
            song_uris.append(uri)
        except IndexError:
            print(f"{song} doesn't exist in Spotify. Skipped.")

    return song_uris


def create_playlist(sp, date, songs_uris):
    user_id = sp.current_user()["id"]
    playlist = sp.user_playlist_create(user=user_id,
                                       name=f"Billboard {date}",
                                       public=False,
                                       description=f"{date} top 100 songs")
    sp.playlist_add_items(playlist_id=playlist["id"], items=songs_uris)


str_date = input(
    "Which year do want to travel to? (i.e. 2021-05-30) ")

billboard_songs = get_billboard_songs(str_date)
sp = get_spotipy_connection()
songs_uris = get_songs_uris(sp, str_date, billboard_songs)
create_playlist(sp, str_date, songs_uris)
