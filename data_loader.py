import pandas as pd
import sqlite3

def load_csv_to_sqlite(csv_path, db_path, table_name):
    df = pd.read_csv(csv_path)
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()

def query_trait_data(db_path, table_name, species_name):
    conn = sqlite3.connect(db_path)
    query = f"SELECT * FROM {table_name} WHERE Scientific_Name LIKE '%{species_name}%'"
    result = pd.read_sql_query(query, conn)
    conn.close()
    return result
