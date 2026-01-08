# 📊 Sentiment Analysis on Amazon Product Reviews

## 📌 Project Overview

This project performs **Sentiment Analysis** on Amazon product reviews using **Natural Language Processing (NLP)** techniques. The goal is to classify customer reviews into **Positive**, **Negative**, or **Neutral** sentiments and visualize sentiment trends to understand customer opinions.

This project is completed as part of **CodeAlpha – Data Analytics Internship (Task 4)**.

---

## 🎯 Objectives

* Analyze textual review data
* Classify sentiments using NLP techniques
* Visualize sentiment distribution
* Extract meaningful insights from customer feedback

---

## 🛠️ Tools & Technologies Used

* **Python**
* **Pandas & NumPy** – Data handling
* **NLTK (VADER Sentiment Analyzer)** – Sentiment analysis
* **Matplotlib & Seaborn** – Data visualization
* **Jupyter Notebook**

---

## 📂 Project Structure

```
Sentiment_Analysis_Project/
│
├── data/
│   └── amazon_reviews.xlsx
│
├── screenshots/
│   ├── dataset_preview.png
│   ├── sentiment_output.png
│   └── sentiment_distribution.png
│
├── sentiment_analysis.ipynb
└── README.md
```

---

## 📥 Dataset Description

The dataset contains Amazon product reviews along with ratings. Each review is analyzed to determine its sentiment.

**Columns:**

* `review` – Customer review text
* `rating` – Product rating (1–5)

---

## 🧠 Methodology

1. Loaded the dataset using Pandas
2. Applied **VADER Sentiment Analyzer** from NLTK
3. Classified reviews into:

   * Positive
   * Neutral
   * Negative
4. Visualized sentiment distribution using bar charts

---

## 📊 Results & Visualizations

* Majority of reviews show **Positive sentiment**
* **Negative sentiment** is mostly associated with low ratings
* **Neutral sentiment** appears in average-rated reviews

These insights help understand customer satisfaction and product performance.

---

## 📸 Screenshots

### 1️⃣ Dataset Preview

Shows the first few rows of the dataset loaded successfully.

📍 *File:* `screenshots/dataset_preview.png`

---

### 2️⃣ Sentiment Classification Output

Displays customer reviews along with their predicted sentiment.

📍 *File:* `screenshots/sentiment_output.png`

---

### 3️⃣ Sentiment Distribution Graph

Visual representation of Positive, Neutral, and Negative reviews.

📍 *File:* `<img width="1118" height="528" alt="Screenshot (378)" src="https://github.com/user-attachments/assets/9baf3dbe-b92a-4cb2-ba72-8fba38e8a7f9" />`

---

## 🚀 Conclusion

Sentiment Analysis helps businesses understand customer opinions and improve decision-making related to marketing, product development, and customer experience. This project demonstrates the practical use of NLP techniques in real-world data analysis.

---

## 🔗 Author

**Vaishnavi V**
Data Analytics Intern – CodeAlpha

---

## 📎 Acknowledgement

Thanks to **CodeAlpha** for providing this internship opportunity and task.
