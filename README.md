# 💼 Machine_Project: Salary Predictor Web App

A Flask web application that predicts whether a job has a **high salary** based on key job-related features.

---

## 🚀 Overview

This project leverages machine learning techniques and a user-friendly web interface to classify job postings as offering either a **high salary** or **not high salary**. It integrates end-to-end functionality from data preprocessing to model deployment using Flask.

---

## 🔍 Key Features

- ✅ **Interactive Web UI** using Flask and HTML.
- ✅ **Real-time Prediction** based on form inputs.
- ✅ **Machine Learning Backend** (Logistic Regression, Random Forest, SVC).
- ✅ **Feature Encoding** and **Selection** using `pd.get_dummies()` and `SelectKBest`.
- ✅ **Model Serialization** using `joblib`.

---

## 📥 Input Fields (via Web Form)

| Field         | Description                            | Example       |
|---------------|----------------------------------------|---------------|
| `Rating`      | Company rating (float)                 | 4.2           |
| `Founded`     | Year the company was founded (integer) | 2010          |
| `Seniority`   | Job seniority level                    | Junior, Senior|
| `State`       | Job location (US state)                | CA, TX        |
| `avg_salary`  | Average salary (numeric)               | 120000        |

---

## 🧠 Machine Learning Pipeline

1. **Data Cleaning** — Handled missing values and outliers using Pandas.
2. **Feature Encoding** — Used `pd.get_dummies()` for categorical variables.
3. **Feature Selection** — Employed `SelectKBest` for dimensionality reduction.
4. **Model Training** — Trained three models:
   - Logistic Regression
   - Random Forest (best performer)
   - Support Vector Classifier (SVC)
5. **Model Saving** — Used `joblib` to store the trained model and selected features.

---

## 📁 Project Structure

```
SalaryApp/
│
├── app.py                 # Flask app server
├── model.pkl              # Trained ML model
├── features.pkl           # List of feature columns after encoding
├── templates/
│   └── index.html         # User input form
├── static/                # (Optional) CSS or JS files
└── README.md              # Documentation (this file)
```

---

## 📈 Model Evaluation

| Model              | Accuracy |
|-------------------|----------|
| Logistic Regression | ~82%    |
| Random Forest       | ~89% ✅ (Best) |
| SVC                 | ~84%    |

The **Random Forest Classifier** gave the best performance and was used in deployment.

## 🌐 Project voiceover
https://drive.google.com/file/d/1uSe1RuGSoKRjv5dptKHBhTu5BX_L1aVz/view?usp=sharing
---

## 🌐 How to Run Locally

Follow these step-by-step instructions to set up and run the web application on your local machine:

### 1. Clone the Repository
Open your terminal or command prompt and run the following commands sequentially:
```bash
git clone [https://github.com/Machine_Project.git](https://github.com/Machine_Project.git)
cd Machine_Project

---

## ✅ Future Improvements

- Add model explanation using SHAP or LIME.
- Extend dataset to improve generalizability.
- Add charts and logs to show model confidence.
- Deploy online using platforms like Heroku or Render.
