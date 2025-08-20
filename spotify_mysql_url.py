import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import mysql.connector

# Spotify credentials
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id='62f3426e19c149f582631441ad73f950',
    client_secret='50da70e0aab74281bc1a2f8c3bd3bb71'
))

# MySQL database config
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'spotify_db'
}

# Connect to MySQL
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

# Tamil playlist ID (Top Tamil 2025)
playlist_id = '0mpwfhIYwjxyS5D2AgufyG'

# Fetch all tracks from playlist
results = sp.playlist_tracks(playlist_id)
tracks = results['items']

# Optional: Get more than 100 tracks if available (pagination)
while results['next']:
    results = sp.next(results)
    tracks.extend(results['items'])

for item in tracks:
    try:
        track = item['track']
        if not track:  # Skip if track data is missing
            continue

        track_data = {
            'Track Name': track['name'],
            'Artist': track['artists'][0]['name'],
            'Album': track['album']['name'],
            'Popularity': track['popularity'],
            'Duration (minutes)': track['duration_ms'] / 60000
        }

        # Insert into MySQL
        insert_query = """
        INSERT INTO spotify_tracks (track_name, artist, album, popularity, duration_minutes)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (
            track_data['Track Name'],
            track_data['Artist'],
            track_data['Album'],
            track_data['Popularity'],
            track_data['Duration (minutes)']
        ))
        connection.commit()

        print(f"Inserted: {track_data['Track Name']} by {track_data['Artist']}")

    except Exception as e:
        print(f"Error processing track: {e}")

# Close connections
cursor.close()
connection.close()

print("All tracks have been processed and inserted into the database.")