import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

results = spotify.artist_albums(birdy_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])



# export SPOTIPY_CLIENT_ID='3750a2d0a4494d3385dbbda87871bab2'
# export SPOTIPY_CLIENT_SECRET='81acd20ff18642b9b9c941d811dfa2de'
# export SPOTIPY_REDIRECT_URI='your-app-redirect-url'