# CoinGecko to PostgreSQL

A small Python pipeline that downloads the full coin list from the
[CoinGecko API](https://www.coingecko.com/en/api), checks every record,
and saves the clean ones in PostgreSQL.

## How it works

```
CoinGecko /coins/list
        |
        v
  fetch     retries with growing waits when the API says "too many requests"
        |
        v
  validate  Pydantic model: id, symbol and name must exist and look right
        |
        +--> rejected records, with the reason, kept for checking
        |
        v
  load      batches of 500 into PostgreSQL, skipping ids that already exist
```

The API returns about 17,000 coins, and not all of them are clean. Some
have strange ids or names made of emoji. Bad records are not dropped
silently. They are collected with the reason they failed, and can be
saved to JSON or CSV with `save_rejected_records`.

Running it twice is safe. The table is only created if it does not exist,
and inserts use `ON CONFLICT DO NOTHING`.

## Project layout

```
src/
  ingestion/   API client and validation step
  models/      Pydantic model for raw data, plain class for clean data
  db/          connection, table setup, batch insert
  utils/       logging and export of rejected records
tests/         pytest tests for the API client
```

## Running it

You need Python 3 and a PostgreSQL database.

```
pip install -r requirements.txt
```

Create a `.env` file:

```
DB_NAME=coins
DB_USER=postgres
DB_PASSWORD=...
DB_HOST=localhost
DB_PORT=5432
```

Then:

```
cd src
python main.py
```

Tests:

```
pytest
```
