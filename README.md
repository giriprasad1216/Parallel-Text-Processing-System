# 📊 Parallel Text Processing & Sentiment Analysis System

## 📌 Project Overview

This project is an end-to-end Text Processing System that performs sentiment analysis on large datasets using parallel processing techniques. It allows users to upload files, process data efficiently, visualize results, and interact through a user-friendly interface.

The system is designed to handle large-scale data and demonstrate the advantages of parallel execution over traditional processing methods.

---

## 🎯 Objectives

- Perform sentiment analysis on text data  
- Implement parallel processing for faster execution  
- Handle large datasets (50K+ records)  
- Provide an interactive UI using Streamlit  
- Enable search, visualization, and export features  

---

## 🏗️ Project Architecture
# 📊 Parallel Text Processing & Sentiment Analysis System

## 📌 Project Overview

This project is an end-to-end Text Processing System that performs sentiment analysis on large datasets using parallel processing techniques. It allows users to upload files, process data efficiently, visualize results, and interact through a user-friendly interface.

The system is designed to handle large-scale data and demonstrate the advantages of parallel execution over traditional processing methods.

---

## 🎯 Objectives

- Perform sentiment analysis on text data  
- Implement parallel processing for faster execution  
- Handle large datasets (50K+ records)  
- Provide an interactive UI using Streamlit  
- Enable search, visualization, and export features  

---

## 🏗️ Project Architecture
# 📊 Parallel Text Processing & Sentiment Analysis System

## 📌 Project Overview

This project is an end-to-end Text Processing System that performs sentiment analysis on large datasets using parallel processing techniques. It allows users to upload files, process data efficiently, visualize results, and interact through a user-friendly interface.

The system is designed to handle large-scale data and demonstrate the advantages of parallel execution over traditional processing methods.

---

## 🎯 Objectives

- Perform sentiment analysis on text data  
- Implement parallel processing for faster execution  
- Handle large datasets (50K+ records)  
- Provide an interactive UI using Streamlit  
- Enable search, visualization, and export features  

---

## 🏗️ Project Architecture
project_folder/
│
├── app.py
├── main.py
├── sentiment_engine.py
├── processor.py
├── database.py
├── search_reviews.py
├── export_csv.py
├── reviews.txt
├── results.db
├── license.txt
└── README.md

---

## ⚙️ Features

### ✅ Core Features

- File Upload (TXT, CSV)  
- Parallel Processing (Multiprocessing & Threading)  
- Sentiment Analysis (Rule-based)  
- Dashboard with metrics  
- Search by keyword  
- CSV Export  

---

### ✅ UI Features (Streamlit)

- Upload file from UI  
- Start processing with button  
- Processing progress indicator  
- Results dashboard  
- Visualization (Pie Chart)  
- Search functionality (supports multiple keywords)  
- Download processed data  
- Clear/Reset results option  
- Custom text sentiment analysis  
- Timestamp display  

---

## 🧠 Sentiment Analysis Logic

The system uses rule-based sentiment analysis.

### ✔️ Positive Words
good, excellent, amazing, beautiful, great, awesome

### ✔️ Negative Words
bad, poor, difficult, worst, slow, problem

---

### ✔️ Special Cases

- "not good" → Negative  
- "very good" → Strong Positive  
- Repeated words:
  - "good good bad" → Score = +1  

---

### ✔️ Score Calculation

- Positive words → +score  
- Negative words → -score  
- Final sentiment:
  - Score > 0 → Positive  
  - Score < 0 → Negative  
  - Score = 0 → Neutral  

---

## ⚡ Parallel Processing

### ✔️ Methods Used

- Single Processing  
- Thread Processing  
- Multiprocessing  

---

### ✔️ How It Works

1. Load input data  
2. Split data into tasks (each review)  
3. Assign tasks to multiple CPU cores  
4. Each worker processes data  
5. Combine results  

---

### ✔️ Performance Insight

- Small dataset → Parallel may be slower  
- Large dataset → Parallel is faster  

---

## 📊 Dashboard Metrics

- Total Records  
- Positive Count  
- Negative Count  

---

## 📈 Visualization

- Pie chart for sentiment distribution  

---

## 🔍 Search Functionality

- Search using keywords  
- Supports:
  - Single word  
  - Multiple words  
  - Repeated words  

---

## 📥 Export Feature

- Download results as CSV  
- Includes:
  - Text  
  - Sentiment  
  - Score  
  - Timestamp  

---

## 🧪 Edge Case Handling

- Empty input  
- Invalid input  
- Repeated words  
- Unknown words  
- Large datasets  

---

## 📂 Dataset Testing

Tested with:
- Small dataset  
- Medium dataset  
- Large dataset (50K+ records)  

---

## 🛠️ Technologies Used

- Python  
- Streamlit  
- Pandas  
- SQLite  
- Matplotlib  
- Multiprocessing  
- Threading  

---

## ▶️ How to Run the Project

### Step 1: Install Libraries

pip install streamlit pandas matplotlib

---

### Step 2: Run Application

streamlit run app.py

---

### Step 3: Open in Browser

http://localhost:8501

---

## 🔄 Workflow

Upload File → Start Processing → Process Data → Store Results → Display Dashboard → Search → Export  

---

## 🎤 Demo Explanation

1. Introduce system  
2. Upload file  
3. Start processing  
4. Show dashboard  
5. Show visualization  
6. Perform search  
7. Download results  

---

## 📌 Key Highlights

- Handles large datasets  
- Uses parallel processing  
- Interactive UI  
- Modular design  
- Real-time analysis  

---

## ⚠️ Limitations

- Rule-based sentiment analysis  
- Accuracy depends on word dictionary  

---

## 🚀 Future Improvements

- Add NLP libraries (NLTK, spaCy)  
- Improve sentiment accuracy  
- Add ML models  

---

## 👩‍💻 Author

Kotha Giriprasad  

---

## 📜 License

This project follows the license provided in `license.txt`.
