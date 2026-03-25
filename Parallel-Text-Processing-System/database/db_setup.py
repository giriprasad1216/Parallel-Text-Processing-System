def clear_table():
    import sqlite3

    conn = sqlite3.connect("results.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM sentiments")

    conn.commit()
    conn.close()