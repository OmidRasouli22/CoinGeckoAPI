from models.coin import Coin

# This is sample data (like what API returns)
sample_data = {
    "id": "bitcoin",
    "symbol": "btc",
    "name": "Bitcoin"
}

# Convert raw dictionary → validated Coin object
coin = Coin(**sample_data)

# Print result
print("Coin object created successfully!")
print(coin)

# Print individual fields
print("ID:", coin.id)
print("Symbol:", coin.symbol)
print("Name:", coin.name)