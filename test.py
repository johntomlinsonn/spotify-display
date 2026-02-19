import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

# Using Spotipy to handle OAuth flow automatically
# This will open a browser to authenticate the user
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv('SPOTIFY_CLIENT_ID'),
    client_secret=os.getenv('SPOTIFY_CLIENT_SECRET'),
    redirect_uri="http://127.0.0.1:8888/callback",
    scope="user-top-read user-read-currently-playing"
))

# Call the API using Spotipy methods
results = sp.currently_playing()


"""
if results and 'items' in results:
    top_tracks = results['items']
    print(top_tracks)
    print(len(top_tracks))
    for track in top_tracks:
        name = track['name']
        artists = ', '.join(artist['name'] for artist in track['artists'])
        print(f'{name} by {artists}')
else:
    print("No top tracks found or error occurred.")

    """


import json

if results:
    with open('currently_playing.json', 'w') as f:
        json.dump(results, f, indent=4)