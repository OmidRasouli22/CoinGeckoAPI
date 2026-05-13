from ingestion.coingecko_api import get_coin_list
import json

def main():
    data = get_coin_list()

    print("TYPE:", type(data))
    print("LENGTH:", len(data))

    # show first 3 items
    print(json.dumps(data[:3], indent=2))

if __name__ == "__main__":
    main()
    

# Output:
# TYPE: <class 'list'>
# LENGTH: 17402
# [
#   {
#     "id": "_",
#     "symbol": "gib",
#     "name": "\u0f3c \u3064 \u25d5_\u25d5 \u0f3d\u3064"
#   },
#   {
#     "id": "000-capital",
#     "symbol": "000",
#     "name": "000 Capital"
#   },
#   {
#     "id": "01111010011110000110001001110100-token",
#     "symbol": "01111010011110000110001001110100",
#     "name": "01111010011110000110001001110100"
#   }
# ]