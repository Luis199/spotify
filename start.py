

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="3750a2d0a4494d3385dbbda87871bab2",
                                                           client_secret="81acd20ff18642b9b9c941d811dfa2de"))

results = sp.search(q='El Alfa', limit=15)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])