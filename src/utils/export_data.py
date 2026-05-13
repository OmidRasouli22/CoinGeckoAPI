import json
import csv
from datetime import datetime
import os


def save_rejected_records(rejected_records, file_format="json"):
    """
    Saves rejected records into a file.

    Args:
        rejected_records: list of rejected items
        file_format: "json" or "csv"
    """

    # Create output folder if not exists
    os.makedirs("data", exist_ok=True)

    # Add timestamp to avoid overwriting files
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    if file_format == "json":
        filename = f"data/rejected_{timestamp}.json"

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(rejected_records, f, indent=2, ensure_ascii=False)

        print(f"Rejected records saved to {filename}")

    elif file_format == "csv":
        filename = f"data/rejected_{timestamp}.csv"

        # Flatten structure for CSV
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)

            # Header
            writer.writerow(["id", "symbol", "name", "reason"])

            for record in rejected_records:
                item = record["item"]

                writer.writerow([
                    item.get("id"),
                    item.get("symbol"),
                    item.get("name"),
                    record["reason"]
                ])

        print(f"Rejected records saved to {filename}")

    else:
        raise ValueError("file_format must be 'json' or 'csv'")