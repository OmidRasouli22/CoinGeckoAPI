import json
import csv
from datetime import datetime
import os


def save_rejected_records(rejected_records, file_format="json"):
    """
    Saves rejected records into a file.
    """

    if not rejected_records:
        print("No rejected records to save.")
        return

    os.makedirs("data", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    if file_format == "json":
        filename = f"data/rejected_{timestamp}.json"

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(rejected_records, f, indent=2, ensure_ascii=False)

        print(f"Rejected records saved to {filename}")

    elif file_format == "csv":
        filename = f"data/rejected_{timestamp}.csv"

        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)

            writer.writerow(["id", "symbol", "name", "reason"])

            for record in rejected_records:
                item = record.get("item", {})
                reason = record.get("reason", "")

                writer.writerow([
                    item.get("id"),
                    item.get("symbol"),
                    item.get("name"),
                    reason
                ])

        print(f"Rejected records saved to {filename}")

    else:
        raise ValueError("file_format must be 'json' or 'csv'")