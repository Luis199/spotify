import os
import sys 
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError


username = sys.argv[1]

# user ID: https://open.spotify.com/user/lghmjq2iawu3ueyt8ugovwvf2?si=S2Nw75lXQtaLHILZ_avz4w


try:
    token = util.prompt_for_user_token(username)
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username)


#Create spotif object
spotifyObject = spotipy.Spotify(auth=token)