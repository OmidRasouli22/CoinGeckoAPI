import requests
import time

BASE_URL = "https://api.coingecko.com/api/v3"


def get_coin_list(max_retries=5):
    url = f"{BASE_URL}/coins/list"

    wait_time = 1  # start with 1 second

    for attempt in range(max_retries):
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()

        # 🔥 Handle rate limit
        if response.status_code == 429:
            print(f"Rate limited. Retrying in {wait_time} seconds...")
            time.sleep(wait_time)
            wait_time *= 2  # exponential backoff
            continue

        # other errors
        raise Exception(f"Error: {response.status_code}")

    raise Exception("Max retries exceeded")