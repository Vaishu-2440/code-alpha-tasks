# CodeAlpha-Task2-EDA README.md

*** CodeAlpha Data Analytics Internship – Task 2  
Exploratory Data Analysis (EDA) ***

A data analytics project focused on performing Exploratory Data Analysis (EDA) using Python and Jupyter Notebook.  

This project demonstrates data understanding, statistical analysis, and visualization on a large sales dataset.

---
## 📋 Table of Contents
Project Overview  
Dataset Description  
Objectives  
Tech Stack  
Project Structure  
EDA Workflow  
Visualizations  
Key Insights  
How to Run the Project  
Notes  
Author  

---

## 📌 Project Overview

This project is completed as part of the **CodeAlpha Data Analytics Internship (Task 2)**.  
The objective of this task is to perform **Exploratory Data Analysis (EDA)** to understand the dataset’s structure, identify patterns, detect anomalies, and explore relationships between variables before further analysis.

---

## 📂 Dataset Description

Dataset Name: `large_sales_dataset.csv`  
Number of Records: 5,000  
Number of Features: 9  

Dataset Columns:
- OrderID – Unique identifier for each order
- CustomerAge – Age of the customer
- Gender – Gender of the customer
- ProductCategory – Category of product purchased
- Quantity – Number of items purchased
- Price – Price per item
- Discount – Discount percentage applied
- PaymentMethod – Mode of payment
- TotalAmount – Final amount after discount

---

## 🎯 Objectives

- Understand the size and structure of the dataset
- Identify numerical and categorical variables
- Generate summary statistics
- Detect missing values and outliers
- Analyze distributions of numerical features
- Explore correlations between numerical variables
- Extract meaningful insights from the data

---

## 🛠️ Tech Stack

Python  
Jupyter Notebook  
Pandas – Data manipulation and analysis  
Matplotlib – Data visualization  
Seaborn – Statistical visualization  

---

## 📁 Project Structure

CodeAlpha_Data_Analytics/
├── Task_2_EDA/
│   ├── large_sales_dataset.csv        # Dataset used for EDA
│   ├── task2_eda.ipynb                # Jupyter Notebook with EDA code
│   ├── README.md                      # Project documentation
│   └── screenshots/
│       ├── histogram.png              # Distribution of numerical features
│       └── correlation_heatmap.png    # Correlation heatmap

---

## 📊 EDA Workflow

The following steps were performed during Exploratory Data Analysis:

1. Dataset loading and preview using `.head()`
2. Dataset structure inspection using `.info()`
3. Summary statistics generation using `.describe()`
4. Missing value detection
5. Distribution analysis using histograms
6. Correlation analysis using a heatmap (numerical features only)
7. Documentation of insights and observations

---

## 📈 Visualizations

Distribution of Numerical Features  
This plot shows the distribution of numerical variables such as age, price, quantity, discount, and total amount.

![Histogram] <img width="1314" height="827" alt="Screenshot (376)" src="https://github.com/user-attachments/assets/3cb620df-809c-4f9a-a02c-4d172ec84ab7" />
<img width="1319" height="268" alt="Screenshot (377)(1)" src="https://github.com/user-attachments/assets/16ae63ab-e067-4e3c-8535-33a036ef0f40" />)


Correlation Heatmap  
This heatmap visualizes correlations between numerical variables and highlights strong relationships.

![Correlation Heatmap] <img width="1319" height="595" alt="Screenshot (377)(2)" src="https://github.com/user-attachments/assets/ec11d738-156d-47fd-b8ac-f1818a83fd1f" />

---

## 🔍 Key Insights

- Quantity and Price strongly influence the TotalAmount
- Discounts reduce the final transaction value
- Customer age distribution shows a diverse customer base
- No missing values were found in the dataset
- Some numerical variables indicate the presence of outliers

---

## ▶️ How to Run the Project

Prerequisites:
- Python 3.x
- Jupyter Notebook
  
Steps:

1. Install required libraries:
   pip install pandas matplotlib seaborn
   
2. Open Jupyter Notebook:
   jupyter notebook

3. Navigate to the `Task_2_EDA` folder

4. Open `task2_eda.ipynb` and run all cells
   
---

## 📝 Notes

- This project focuses only on Exploratory Data Analysis
- No machine learning models are implemented
- The dataset is synthetically generated for learning purposes
- This project is intended for internship evaluation and educational use
  
---

## 👨‍💻 Author

Sri Vaishnavi Vedantam 
CodeAlpha Data Analytics Internship  

---

## 📄 License

This project is created for educational and internship evaluation purposes only.
