
# Spotify Streaming Data Analyzer

This script processes Spotify streaming history data to generate monthly listening reports.
It reads JSON export files from Spotify, processes the streaming data, and creates a CSV
report summarizing listening habits for a specific month.

Its pretty simple you can definitly extend it. This is just a random project I started years ago lol

**Functionality:**

1. Loads multiple Spotify streaming history JSON files
2. Filters data for a specific month (and optionally year)
3. Calculates total minutes played for each track
4. Aggregates data by track and artist
5. Generates a sorted CSV report of most-played songs

**Key Features:**

- Handles multiple input files (typical Spotify exports are split)
- Converts milliseconds played to minutes
- Groups and aggregates data by track and artist
- Sorts results by total listening time
- Outputs clean CSV format for easy analysis(Maybe you can make your own Spotify Wrapped🤷🏾‍♂️🤔)

**Usage:**
The script is designed to process Spotify's "Extended streaming history" JSON exports obtained from:
[Spotify Privacy Page](https://www.spotify.com/us/account/privacy/)

**Typical Input Files:**

- StreamingHistory_music_0.json
- StreamingHistory_music_1.json
- etc.

Output:
A CSV file containing columns: Track, Artist, Minutes Played
Sorted in descending order by total minutes played

Example:
get_month_report(spotify_data, "07") generates a report for July listening statistics
