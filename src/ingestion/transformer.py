from pydantic import ValidationError

from models.coin import Coin
from models.coin_model import CoinModel
from utils.logger import get_logger

logger = get_logger("transformer")


def transform_coins(raw_data):
    """
    This function takes raw API data and converts it into clean Coin objects.

    Steps:
    1. Validate raw data using Pydantic schema
    2. Convert validated data into internal Coin objects
    3. Collect rejected records for debugging
    """

    cleaned_coins = []
    rejected_records = []

    for item in raw_data:

        try:
            # First step: validate the raw input data
            validated = CoinModel(**item)

            # Second step: convert validated data into internal model
            coin = Coin(
                id=validated.id,
                symbol=validated.symbol,
                name=validated.name
            )

            cleaned_coins.append(coin)

        except ValidationError as e:
            rejected_records.append({
                "item": item,
                "reason": str(e)
            })

            logger.warning(
                f"Rejected coin: {item.get('id')} because validation failed"
            )

        except Exception as e:
            rejected_records.append({
                "item": item,
                "reason": str(e)
            })

            logger.error(
                f"Unexpected error while processing coin: {item.get('id')} - {e}"
            )

    logger.info(f"Valid coins: {len(cleaned_coins)}")
    logger.info(f"Rejected coins: {len(rejected_records)}")

    return cleaned_coins, rejected_records