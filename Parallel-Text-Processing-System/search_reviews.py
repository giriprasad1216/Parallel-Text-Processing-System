import sqlite3

def search_menu():

    conn = sqlite3.connect("results.db")
    cursor = conn.cursor()

    while True:

        print("\n---- SEARCH MENU ----")
        print("1. Show Positive Reviews")
        print("2. Show Negative Reviews")
        print("3. Search by Keyword")
        print("4. Filter by Score")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":

            cursor.execute("SELECT review, sentiment, score FROM sentiments WHERE sentiment='Positive'")
            rows = cursor.fetchall()

            for row in rows:
                print(row)

        elif choice == "2":

            cursor.execute("SELECT review, sentiment, score FROM sentiments WHERE sentiment='Negative'")
            rows = cursor.fetchall()

            for row in rows:
                print(row)

        elif choice == "3":

            keyword = input("Enter keyword: ")

            cursor.execute(
                "SELECT review, sentiment, score FROM sentiments WHERE review LIKE ?",
                ('%' + keyword + '%',)
            )

            rows = cursor.fetchall()

            for row in rows:
                print(row)

        elif choice == "4":

            score = input("Enter minimum score: ")

            cursor.execute(
                "SELECT review, sentiment, score FROM sentiments WHERE score >= ?",
                (score,)
            )

            rows = cursor.fetchall()

            for row in rows:
                print(row)

        elif choice == "5":

            print("Exiting search menu")
            break

    conn.close()