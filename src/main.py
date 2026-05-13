import json
from ingestion.coingecko_api import get_coin_list

def main():
    data = get_coin_list()
    print(json.dumps(data[:10], indent=2))  # first 10 items only

if __name__ == "__main__":
    main()