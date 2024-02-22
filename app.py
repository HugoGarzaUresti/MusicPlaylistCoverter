import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
from ytmusicapi import YTMusic


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='89160bbbc4a64653b45297b746cca141',
                                                   client_secret='0992482a5cea404889788cb116ad8de8',
                                                   redirect_uri='http://localhost:8000/callback',
                                                   scope='playlist-read-private'))

user_profile = sp.current_user()

# Print profile data
print(user_profile)