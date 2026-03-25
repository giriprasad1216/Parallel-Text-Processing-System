# main.py

import time
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool

from sentiment_engine import analyze_sentiment
from database import create_table, insert_results, create_index
from search_reviews import search_menu
from export_csv import export_to_csv


# ---------------------------------
# Load Reviews
# ---------------------------------

def load_reviews():

    with open("reviews.txt", "r", encoding="utf-8") as file:
        reviews = file.readlines()

    reviews = [review.strip() for review in reviews]

    return reviews


# ---------------------------------
# Wrapper Function (UPDATED)
# ---------------------------------

def process_review(review):

    sentiment, score, timestamp = analyze_sentiment(review)

    return (review, sentiment, score, timestamp)


# ---------------------------------
# Single Processing
# ---------------------------------

def single_processing(reviews):

    results = []

    start_time = time.time()

    for review in reviews:
        result = process_review(review)
        results.append(result)

    end_time = time.time()

    print("Single Processing Time:", end_time - start_time)

    return results


# ---------------------------------
# Thread Processing
# ---------------------------------

def thread_processing(reviews):

    start_time = time.time()

    with ThreadPoolExecutor() as executor:
        results = list(executor.map(process_review, reviews))

    end_time = time.time()

    print("Thread Processing Time:", end_time - start_time)

    return results


# ---------------------------------
# Multiprocessing (PARALLEL)
# ---------------------------------

def multiprocessing_processing(reviews):

    start_time = time.time()

    with Pool() as pool:
        results = pool.map(process_review, reviews)

    end_time = time.time()

    print("Multiprocessing Time:", end_time - start_time)

    return results


# ---------------------------------
# Query Performance Test
# ---------------------------------

def query_test():

    import sqlite3

    conn = sqlite3.connect("results.db")
    cursor = conn.cursor()

    start = time.time()

    cursor.execute("SELECT * FROM sentiments WHERE sentiment='Positive'")
    rows = cursor.fetchall()

    end = time.time()

    print("Query Time:", end - start)

    conn.close()


# ---------------------------------
# Main Program
# ---------------------------------

if __name__ == "__main__":

    print("\nStarting Milestone 3 Processor...")

    create_table()
    create_index()

    reviews = load_reviews()

    print("Total Reviews:", len(reviews))

    single_results = single_processing(reviews)
    thread_results = thread_processing(reviews)
    multi_results = multiprocessing_processing(reviews)

    insert_results(multi_results)

    print("\nResults stored in database")

    query_test()

    print("\nExporting results to CSV...")
    export_to_csv()

    print("\nOpening search menu...")
    search_menu()

    print("\nProgram Completed")