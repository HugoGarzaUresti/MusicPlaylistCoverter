# MusicPlaylistCoverter
## Description
This application facilitates the transfer of playlists from Spotify to YouTube Music. It leverages the Spotify Web API and the unofficial YouTube Music API (ytmusicapi) to fetch playlists from a user's Spotify account and recreate them in their YouTube Music account.

## Prerequisites
Before you begin, ensure you have the following:

Python 3.6 or later installed on your system.
A Spotify Developer account and a registered application to obtain the client_id and client_secret.
Access to your YouTube Music account to set up ytmusicapi.

## Setup
Step 1: Clone the Repository
Clone this repository to your local machine using git clone, followed by the repository URL.

Step 2: Install Dependencies
Navigate to the project directory and install the required Python packages:

Python
'''
pip install spotipy ytmusicapi requests
'''
Step 3: Spotify API Setup
Go to the Spotify Developer Dashboard and create a new application.
Note down the Client ID and Client Secret.
Set the Redirect URI in your Spotify app settings to http://localhost:8000/callback.
Step 4: YouTube Music API Setup
Follow the ytmusicapi setup instructions to authenticate your YouTube Music account. This typically involves generating a headers_auth.json file.
Place the headers_auth.json file in your project directory.
Configuration
Create a .env file in the root of your project directory and add your Spotify Client ID and Client Secret:

Python
'''
SPOTIFY_CLIENT_ID='your_spotify_client_id_here'
SPOTIFY_CLIENT_SECRET='your_spotify_client_secret_here'
'''
## Usage
To run the application, execute the main script from the command line:

Console
'''
python main.py
'''
Follow any on-screen prompts to authenticate your Spotify account and start the playlist transfer process.

## Troubleshooting
Ensure you have internet access and that your Spotify and YouTube Music accounts are active.
Verify that your Spotify Client ID, Client Secret, and Redirect URI are correctly configured.
Check the headers_auth.json file for YouTube Music to ensure it's correctly set up.

## Contributing
Contributions to improve the application are welcome. Please follow the standard fork-pull request workflow.
