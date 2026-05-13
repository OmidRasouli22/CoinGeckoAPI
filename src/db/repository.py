from psycopg2.extras import execute_batch

BATCH_SIZE = 500

def chunk_list(data, chunk_size):
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]

def insert_coins_batch(conn, coins):
    """
    Inserts multiple coin records into the database using batch processing.
    """
    cursor = conn.cursor()
    insert_query = """
    INSERT INTO coins (id, symbol, name)
    VALUES (%s, %s, %s)
    ON CONFLICT (id) DO NOTHING;
    """
    try:
        total_inserted = 0

        # Step 1: Split data into chunks
        for chunk in chunk_list(coins, BATCH_SIZE):

            # Step 2: Convert Coin objects → tuples
            data = [(coin.id, coin.symbol, coin.name) for coin in chunk]

            # Step 3: Insert one chunk at a time
            execute_batch(cursor, insert_query, data)
            conn.commit()

            total_inserted += len(chunk)

            print(f"Inserted chunk: {len(chunk)} | Total: {total_inserted}")

        print(f"Finished inserting {total_inserted} coins.")

    except Exception as e:
        conn.rollback()
        print(f"Error inserting coins: {e}")

    finally:
        cursor.close()