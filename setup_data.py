import pandas as pd
import sqlite3

def clean_and_load(csv_path, db_path, table_name, rename_map, drop_cols=None):
    df = pd.read_csv(csv_path)
    df.rename(columns=rename_map, inplace=True)
    if drop_cols:
        df.drop(columns=drop_cols, inplace=True, errors='ignore')
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()
    print(f"✅ Loaded {table_name} into {db_path} with {len(df)} rows.")

# Rename mappings
avonet_rename = {
    "Species1": "Scientific_Name",
    "Family1": "Family",
    "Order1": "Order",
    "Beak.Length_Culmen": "Beak_length_mm",
    "Wing.Length": "Wing_length_mm",
    "Mass": "Body_mass_g"
}

avilist_rename = {
    "Scientific_name": "Scientific_Name",
    "English_name_Clements_v2024": "Common_Name",
    "Order": "Order",
    "Family": "Family"
}

legcolor_rename = {
    "Scientific name": "Scientific_Name",
    "Common name": "Common_Name",
    "Leg Color (Pri/Male)\n(Logan)": "Leg_Color"
}

# Clean and load
clean_and_load("data/avonet.csv", "db/bird_data.db", "avonet", avonet_rename)
clean_and_load("data/avilist.csv", "db/bird_data.db", "avilist", avilist_rename)
clean_and_load("data/bird_leg_color.csv", "db/bird_data.db", "bird_leg_color", legcolor_rename)