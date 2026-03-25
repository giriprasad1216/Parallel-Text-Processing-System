import sqlite3
import csv

def export_to_csv():
    conn = sqlite3.connect("results.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM sentiments")
    rows = cursor.fetchall()

    with open("output.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Chunk", "Sentiment", "Score"])
        writer.writerows(rows)

    conn.close()