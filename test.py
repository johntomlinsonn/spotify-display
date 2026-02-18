import os
from dotenv import load_dotenv
import requests

load_dotenv()

#ENV vars
token = os.getenv('SPOTIFY_TOKEN')

#overall function to fetch data from spotify web api
def fetch_web_api(endpoint, method, body):
    res = requests.request(method, f'https://api.spotify.com/{endpoint}', headers={
        'Authorization': f'Bearer {token}',
    }, json=body)
    return res.json()


def get_top_tracks():
    return fetch_web_api('v1/me/top/tracks?time_range=long_term&limit=5', 'GET', None)['items']


top_tracks = get_top_tracks()
print(len(top_tracks))
for track in top_tracks:
    name = track['name']
    artists = ', '.join(artist['name'] for artist in track['artists'])
    print(f'{name} by {artists}')