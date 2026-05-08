from config import DB_URL
from src.data_access.query_runner import run_query
from src.data_access.data_extractor import save_to_csv

# Read the query from the sql file 
with open("sql/extracted_raw_data.sql", "r") as f:
    query = f.read()

df = run_query(DB_URL, query)
save_to_csv(df, "data/raw/raw-data.csv")