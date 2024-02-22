from spotipy.oauth2 import SpotifyOAuth
import requests
from ytmusicapi import YTMusic
import json

ytmusic = YTMusic("browser.json")

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='89160bbbc4a64653b45297b746cca141',
                                               client_secret='0992482a5cea404889788cb116ad8de8',
                                               redirect_uri='http://172.29.27.39:8000/callback',
                                               scope='user-read-private'))
pl_id = []
tracks_ids = []
yt_tracks_id = []
def get_PlaylistID():
    pl=sp.current_user_playlists()
    for playlist in pl["items"]:
        pl_id.append(playlist["id"])

def get_playtlistTracks(playlistID):
    tracks = {}
    tracks = sp.playlist_tracks(playlistID)
    for track in tracks["items"]:
        tracks_ids.append(track["track"]["id"])


def main():
    get_PlaylistID()
    currentPL = pl_id[2]
    get_playtlistTracks(pl_id[2])
    for ids in tracks_ids:
        track_info = sp.track(ids)
        search_query = track_info['name'] + '' + track_info['artists'][0]['name']
        search_results = ytmusic.search(search_query, filter='songs')
        if search_results:
            yt_tracks_id.append(search_results[0]['videoId'])
    for yt_track_id in yt_tracks_id:
        song = ytmusic.get_song(yt_track_id)
        if song and 'videoDetails' in song:
            print(song['videoDetails']['title'])

    playlist_id = ytmusic.create_playlist(sp.playlist(currentPL)["name"], 'Created from Spotify')
    ytmusic.add_playlist_items(playlist_id, yt_tracks_id)

    

if __name__ == '__main__':
    main()
