from models.coin import Coin
import re

# Detect weird emoji / unicode patterns (common in junk tokens)
WEIRD_CHAR_PATTERN = re.compile(r"[༼◕つ]")

# Detect IDs that are just numbers or encoded junk
NUMERIC_ID_PATTERN = re.compile(r"^[0-9\-]+$")


from utils.logger import get_logger
logger = get_logger("transformer")

def is_valid_coin_data(item: dict) -> (bool, str):
    """
    This function decides whether a coin is "clean enough" to use.

    We reject:
    - missing fields
    - garbage names (emoji / weird symbols)
    - encoded / spam token IDs
    - extremely long or unrealistic symbols
    """

    # 1. Must have required fields
    if not item.get("id") or not item.get("symbol") or not item.get("name"):
        return False, "Missing required fields"

    # 2. Symbol should not be too long
    symbol = item["symbol"]
    if len(symbol) > 15:
         return False, "Symbol too long"

    # 3. Reject very long "encoded" token IDs
    if item["id"].endswith("-token") and len(item["id"]) > 30:
        return False, "Encoded token ID too long"

    # 4. Reject weird emoji-based names
    name = item["name"]
    if WEIRD_CHAR_PATTERN.search(name):
        return False, "Invalid coin name"

    # 5. Reject purely numeric or encoded IDs
    if NUMERIC_ID_PATTERN.fullmatch(item["id"]):
        return False, "Invalid coin ID"

    return True, "Valid coin data"


def transform_coins(raw_data):
    """
    This function:
    1. Filters bad data
    2. Converts valid data into Coin objects
    """

    cleaned_coins = []
    rejected_records = []

    for item in raw_data:
        is_valid, reason = is_valid_coin_data(item)
        
        if not is_valid:
            rejected_records.append((item, reason))
            logger.warning(f"Rejected record: {item} - Reason: {reason}")

        try:
            # Step 2: Convert dictionary → Coin object
            coin = Coin(
                id=item.get("id"),
                symbol=item.get("symbol"),
                name=item.get("name")
            )

            cleaned_coins.append(coin)

        except Exception as e:
            rejected_records.append({
                "item": item,
                "reason": str(e)
            })

            logger.error(f"Validation failed: {item.get('id')} | Error: {e}")


    logger.info(f"Total valid coins: {len(cleaned_coins)}")
    logger.info(f"Total rejected coins: {len(rejected_records)}")
    
    return cleaned_coins, rejected_records