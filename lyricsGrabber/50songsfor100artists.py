import csv
import lyricsgenius
import time
from requests.exceptions import Timeout
from concurrent.futures import ThreadPoolExecutor, as_completed

# Initialize the Genius API client with a longer timeout
genius = lyricsgenius.Genius("MpY2-SgiN1WZygcE3lXZiRZFnyTcWG8zQBVSyLZGVYnX9Hc607mreDQlvYXoQfDt", timeout=10)

# Function to fetch songs for an artist
def fetch_songs(artist_name):
    try:
        artist = genius.search_artist(artist_name, max_songs=50, include_features=False)
        return [(song.title, artist_name) for song in artist.songs]
    except Timeout:
        print(f"Timeout error for artist {artist_name}.")
        return []

# File paths
input_csv = '100-artists.csv'   # Path to your input CSV containing artist names
output_csv = 'songs2.csv'    # Path to your output CSV for saving song titles

# Open the input CSV and output CSV
with open(input_csv, mode='r') as infile, open(output_csv, mode='w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Use ThreadPoolExecutor to fetch songs concurrently
    with ThreadPoolExecutor(max_workers=98) as executor:  # Adjust max_workers as needed
        futures = {executor.submit(fetch_songs, row[0]): row[0] for row in reader}

        for future in as_completed(futures):
            artist_name = futures[future]
            try:
                songs = future.result()
                for song_title, artist in songs:
                    writer.writerow([song_title, artist])
            except Exception as e:
                print(f"Error fetching songs for artist {artist_name}: {e}")
