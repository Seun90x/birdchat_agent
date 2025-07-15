import requests
import sqlite3
from dotenv import load_dotenv
import os

load_dotenv()
EBIRD_API_KEY = os.getenv("EBIRD_API_KEY")

CACHE_DB = "db/bird_data.db"

# -- Helper: get species code from name using avilist
def get_species_code(scientific_name):
    conn = sqlite3.connect(CACHE_DB)
    cur = conn.cursor()
    query = f"SELECT `Species_code_Cornell_Lab` FROM avilist WHERE `Scientific_Name` = ?"
    cur.execute(query, (scientific_name,))
    row = cur.fetchone()
    conn.close()
    return row[0] if row else None

# -- Helper: call eBird API
def ebird_request(endpoint, params=None):
    headers = {"X-eBirdApiToken": EBIRD_API_KEY}
    url = f"https://api.ebird.org/v2/{endpoint}"
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"eBird API error {response.status_code}: {response.text}")
        return None

# -- Get taxonomy summary
def get_taxonomy_info(species_code):
    return ebird_request(f"ref/taxonomy/ebird?fmt=json")

# -- Get recent sightings (worldwide)
def get_recent_sightings(species_code):
    return ebird_request(f"data/obs/geo/recent/{species_code}", params={"lat": 0, "lng": 0})

# -- Get general info given species name
def query_ebird(scientific_name):
    code = get_species_code(scientific_name)
    if not code:
        return f"❌ Could not find species code for '{scientific_name}'."

    sightings = get_recent_sightings(code)
    if sightings:
        location = sightings[0].get("locName", "unknown location")
        date = sightings[0].get("obsDt", "unknown date")
        return f"🕊️ Recent sighting of {scientific_name} at {location} on {date}."
    else:
        return f"No recent sightings for {scientific_name} found."

if __name__ == "__main__":
    # Simple test
    print(query_ebird("Opisthocomus hoazin")) # Should return recent sighting info for Chicken

# Example usage:
# result = query_ebird("Turdus migratorius")
# print(result)  # Should return recent sighting info for American Robin
# This code provides functions to query the eBird API for bird species information, including taxonomy and recent sightings. 
# It uses a SQLite database to cache species codes and allows users to retrieve recent sightings based on scientific names. 
# The main function demonstrates how to query the eBird API for a specific species (American Robin) and print the result. 
# The code includes error handling for cases where species codes or sightings are not found, ensuring robustness in the querying process.
# Note: Make sure to set the EBIRD_API_KEY in your .env file for this code to work.
# Also, ensure that the SQLite database (db/bird_data.db) contains the necessary tables and data for the queries to function correctly. 