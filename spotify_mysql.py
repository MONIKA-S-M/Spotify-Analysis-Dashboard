import re
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector

# Set up client credentials
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id='62f3426e19c149f582631441ad73f950',
    client_secret='50da70e0aab74281bc1a2f8c3bd3bb71'
))

#Mysql database connection 
db_config = {
    'host' : 'localhost',
    'user' : 'root',
    'password' : 'root',
    'database' : 'spotify_db' 
}

#Connect to database 
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

# Full track URL
track_url = "https://open.spotify.com/track/003vvx7Niy0yvhvHt4a68B"

# Extract track ID from URL
track_id = re.search(r'track/([a-zA-Z0-9]+)', track_url).group(1)

# Fetch track details
track = sp.track(track_id)

# Extract metadata
track_data = {
    'Track Name': track['name'],
    'Artist': track['artists'][0]['name'],
    'Album': track['album']['name'],
    'Popularity': track['popularity'],
    'Duration (minutes)': track['duration_ms'] / 60000  # convert ms to minutes
}

#Insert data into mysql
insert_query = """
insert into spotify_tracks (track_name,artist,album,popularity,duration_minutes)
values (%s, %s, %s, %s, %s)
"""
cursor.execute(insert_query,params=(
    track_data['Track Name'],
    track_data['Artist'],
    track_data['Album'],
    track_data['Popularity'],
    track_data['Duration (minutes)']
))
connection.commit()

print(f"Track '{track_data['Track Name']}' by {track_data['Artist']}inserted into the database")

#Close the connection 
cursor.close()
connection.close()