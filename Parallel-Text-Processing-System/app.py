# app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sentiment_engine import analyze_sentiment

# -------------------------
# Session State
# -------------------------
if "results_df" not in st.session_state:
    st.session_state.results_df = None

st.set_page_config(page_title="Text Processing System", layout="wide")

st.title("Parallel Text Processing Dashboard")

# -------------------------
# 🔥 Custom Text Analysis (FIXED - NO REDIRECT)
# -------------------------
st.subheader("Analyze Custom Text")

custom_text = st.text_input("Enter any text to analyze", key="custom_input")

if custom_text:
    sentiment, score, timestamp = analyze_sentiment(custom_text)

    st.write("Sentiment:", sentiment)
    st.write("Score:", score)
    st.write("Timestamp:", timestamp)

# -------------------------
# Sidebar
# -------------------------
st.sidebar.header("Upload and Processing")

uploaded_file = st.sidebar.file_uploader(
    "Upload Text or CSV File",
    type=["txt", "csv"]
)

start_button = st.sidebar.button("Start Processing")
reset_button = st.sidebar.button("Clear Results")

reviews = []

# -------------------------
# Reset Button
# -------------------------
if reset_button:
    st.session_state.results_df = None
    st.success("Data Cleared Successfully")

# -------------------------
# File Preview
# -------------------------
if uploaded_file is not None:

    st.subheader("File Preview")

    if uploaded_file.type == "text/plain":
        text = uploaded_file.read().decode("utf-8")
        reviews = text.split("\n")
        st.text(text[:500])

    elif uploaded_file.type == "text/csv":
        df = pd.read_csv(uploaded_file)
        reviews = df.iloc[:, 0].astype(str).tolist()
        st.dataframe(df)

    st.write("Files Uploaded: 1")
    st.write("Total Records:", len(reviews))

# -------------------------
# Processing
# -------------------------
if start_button and reviews:

    progress_bar = st.progress(0)

    results = []

    for i, review in enumerate(reviews):

        sentiment, score, timestamp = analyze_sentiment(review)

        results.append({
            "Text": review,
            "Sentiment": sentiment,
            "Score": score,
            "Timestamp": timestamp
        })

        progress_bar.progress((i + 1) / len(reviews))

    st.session_state.results_df = pd.DataFrame(results)

    st.success("Processing Completed")

# -------------------------
# Display Results
# -------------------------
if st.session_state.results_df is not None:

    results_df = st.session_state.results_df

    st.subheader("Results Dashboard")
    st.dataframe(results_df)

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Records", len(results_df))
    col2.metric("Positive", (results_df["Score"] > 0).sum())
    col3.metric("Negative", (results_df["Score"] < 0).sum())

    # -------------------------
    # Visualization (FIXED)
    # -------------------------
    st.subheader("Visualization")

    counts = results_df["Sentiment"].value_counts()

    fig, ax = plt.subplots()
    ax.pie(counts, labels=counts.index, autopct="%1.1f%%")
    st.pyplot(fig)

    # -------------------------
    # 🔥 SEARCH (MULTI-WORD FIXED)
    # -------------------------
    st.subheader("Search Results")

    keyword = st.text_input("Search Keyword", key="search_input")

    if keyword:

        search_words = keyword.lower().split()

        filtered_df = results_df[
            results_df["Text"].str.lower().apply(
                lambda x: any(word in x for word in search_words)
            )
        ]

        if not filtered_df.empty:
            st.dataframe(filtered_df)
        else:
            st.warning("No matching results found")

    # -------------------------
    # Download CSV
    # -------------------------
    csv = results_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "Download CSV",
        csv,
        "results.csv",
        "text/csv"
    )