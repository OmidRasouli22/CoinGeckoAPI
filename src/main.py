from ingestion.coingecko_api import get_coin_list
from ingestion.transformer import transform_coins
from utils.export_data import save_rejected_records

def main():
    # 1. Fetch raw data from API
    raw_data = get_coin_list()

    print("Raw data received:", len(raw_data))

    # 2. Transform raw data → clean objects
    valid_coins, rejected_records = transform_coins(raw_data)

    print("Clean coins created:", len(valid_coins))
    print("Rejected records:", len(rejected_records))

    # save rejected records for debugging
    file_format = input("Choose format to save rejected data (json/csv): ").strip().lower()

    if rejected_records:
        save_rejected_records(rejected_records, file_format=file_format)

if __name__ == "__main__":
    main()