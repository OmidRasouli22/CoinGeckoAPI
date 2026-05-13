from ingestion.coingecko_api import get_coin_list
from ingestion.transformer import transform_coins

def main():
    # 1. Fetch raw data from API
    raw_data = get_coin_list()

    print("Raw data received:", len(raw_data))

    # 2. Transform raw data → clean objects
    coins = transform_coins(raw_data)

    print("Clean coins created:", len(coins))

    # 3. Show sample output
    print("\nSample coins:")
    print(coins[0: 10])

if __name__ == "__main__":
    main()