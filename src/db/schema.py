from db.connection import get_connection


def create_tables():
    """
    Ensures required tables exist in the database.
    """

    conn = get_connection()
    cursor = conn.cursor()

    # SQL to create coins table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS coins (
        id TEXT PRIMARY KEY,
        symbol TEXT,
        name TEXT
    );
    """

    try:
        cursor.execute(create_table_query)
        conn.commit()
        print("Table 'coins' ensured.")

    except Exception as e:
        conn.rollback()
        print(f"Error creating table: {e}")

    finally:
        cursor.close()
        conn.close()