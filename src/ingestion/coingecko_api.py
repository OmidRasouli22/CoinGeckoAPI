import requests

# Base URL for CoinGecko API
BASE_URL = "https://api.coingecko.com/api/v3"

def get_coin_list():
    """Fetch the list of all coins from CoinGecko."""
    url = f"{BASE_URL}/coins/list"
    response = requests.get(url)
    
    response.raise_for_status()
    
    return response.json()