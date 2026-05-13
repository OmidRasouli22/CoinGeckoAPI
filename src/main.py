from db.connection import get_connection
from db.repository import insert_coins_batch
from ingestion.coingecko_api import get_coin_list
from ingestion.transformer import transform_coins
from utils.export_data import save_rejected_records
from db.schema import create_tables


def main():
    # 1. Fetch raw data from API
    raw_data = get_coin_list()

    # print("Raw data received:", len(raw_data))

    # 2. Transform raw data → clean objects
    valid_coins, rejected_records = transform_coins(raw_data)

    print("Clean coins created:", len(valid_coins))
    print("Rejected records:", len(rejected_records))

    # save rejected records for debugging
    # if rejected_records:
        # save_rejected_records(rejected_records, file_format="json")
        
    conn = get_connection()

    # create tables if they don't exist (safe to run multiple times)
    create_tables()
    
    # Insert only a subset first (safe testing)
    insert_coins_batch(conn, valid_coins)

    conn.close()

    print("Data inserted successfully!")

if __name__ == "__main__":
    main()