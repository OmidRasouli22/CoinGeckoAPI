from psycopg2.extras import execute_batch

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
        data = [(coin.id, coin.symbol, coin.name) for coin in coins]

        execute_batch(cursor, insert_query, data)
        
        conn.commit()
        print(f"Inserted {len(coins)} coins.")
    except Exception as e:
        conn.rollback()
        print(f"Error inserting coins: {e}")
    finally:
        cursor.close()