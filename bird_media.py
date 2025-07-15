import sqlite3
from ebird_api import get_species_code

CACHE_DB = "db/bird_data.db"

def get_species_code(scientific_name):
    conn = sqlite3.connect(CACHE_DB)
    cur = conn.cursor()
    query = "SELECT Species_code_Cornell_Lab FROM avilist WHERE LOWER(Scientific_Name) = LOWER(?)"
    cur.execute(query, (scientific_name.strip(),))
    row = cur.fetchone()
    conn.close()
    return row[0] if row else None

def get_macaulay_photo_url(scientific_name):
    species_code = get_species_code(scientific_name)
    if not species_code:
        return f"📸 No exact match found for '{scientific_name}'. You can try searching manually:\nhttps://search.macaulaylibrary.org/catalog?mediaType=photo&taxonFilter={scientific_name.replace(' ', '%20')}"
    return f"https://search.macaulaylibrary.org/catalog?taxonCode={species_code}&mediaType=photo"

if __name__ == "__main__":
    print(get_macaulay_photo_url("Turdus migratorius"))  # Should return the photo URL for American Robin
    print(get_macaulay_photo_url("Gallus gallus"))  # Should return the photo URL for Chicken
    print(get_macaulay_photo_url("Unknown species"))  # Should return an error message
    print(get_macaulay_photo_url("Passer domesticus"))  # Should return the photo URL for House Sparrow