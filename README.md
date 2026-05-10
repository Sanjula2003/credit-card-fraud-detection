# 🚨 AI-Powered Credit Card Fraud Detection System

A real-time Machine Learning dashboard that analyzes transaction risk and predicts fraudulent credit card activity using XGBoost and risk-based AI decisioning.

---

# 🚀 Live Demo

🔗 Live App: YOUR_STREAMLIT_LINK_HERE

🔗 GitHub Repository: https://github.com/Sanjula2003/credit-card-fraud-detection

---

# 📌 Project Overview

This project is an end-to-end fraud detection system designed to identify suspicious credit card transactions using Machine Learning and real-time risk analysis.

The system uses an XGBoost classification model trained on highly imbalanced transaction data and applies SMOTE (Synthetic Minority Oversampling Technique) to improve fraud detection performance.

A modern Streamlit dashboard was developed to simulate a real-world fintech fraud monitoring interface with:
- fraud probability scoring
- risk-level classification
- decision recommendations
- real-time transaction analysis

---

# 🎯 Key Features

- Real-time fraud detection
- XGBoost Machine Learning model
- SMOTE imbalance handling
- Fraud probability scoring
- Risk-based transaction classification
- Approve / Review / Block decision system
- Interactive fintech-style dashboard
- Business-friendly transaction inputs
- Dark modern UI
- Deployment-ready Streamlit application

---

# 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Imbalanced-learn (SMOTE)
- Streamlit
- Joblib
- Matplotlib

---

# 🤖 Machine Learning Workflow

1. Loaded and analyzed credit card transaction dataset
2. Performed exploratory data analysis (EDA)
3. Identified severe class imbalance
4. Applied feature scaling
5. Split data into training and testing sets
6. Used SMOTE to balance fraud samples
7. Trained Logistic Regression baseline model
8. Trained advanced XGBoost classifier
9. Evaluated models using:
   - Precision
   - Recall
   - F1-score
10. Saved trained model for deployment
11. Built interactive Streamlit dashboard

---

# 📊 Dataset Information

The project uses the popular Credit Card Fraud Detection dataset containing anonymized transaction features.

> Note: The original dataset is not included in this repository due to file size limitations. It can be downloaded from Kaggle.

### Target Variable

| Class | Meaning |
|---|---|
| 0 | Normal Transaction |
| 1 | Fraudulent Transaction |

The dataset is highly imbalanced, making fraud detection a real-world anomaly detection problem.

---

# 📈 Dashboard Features

## Transaction Analysis
- Transaction amount input
- Transaction hour analysis
- Risk indicator simulation

## Fraud Prediction
- Fraud probability score
- Normal transaction probability
- Real-time ML prediction

## Risk Decision Engine
- Low Risk → Approve
- Medium Risk → Manual Review
- High Risk → Block Transaction

---

# 📂 Project Structure

```text
credit-card-fraud-detection/
│
├── app.py
├── fraud_detection_model.pkl
├── feature_names.pkl
├── requirements.txt
├── README.md
├── data/
└── notebooks/
```

---

# ▶️ Run Locally

Clone repository:

```bash
git clone https://github.com/Sanjula2003/credit-card-fraud-detection.git
```

Go to project folder:

```bash
cd credit-card-fraud-detection
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run Streamlit app:

```bash
streamlit run app.py
```

---

# 📚 What I Learned

Through this project, I gained hands-on experience in:

- Fraud detection systems
- Imbalanced Machine Learning
- SMOTE oversampling
- XGBoost classification
- Financial risk analytics
- ML model evaluation
- Streamlit dashboard development
- AI deployment workflows
- Business-focused AI product design

---

# ⚠️ Disclaimer

This project is developed for educational and portfolio purposes only. It should not be used as a production financial fraud prevention system without further testing and enterprise-level security validation.

---

# 👨‍💻 Author

**Sanjula2003**

GitHub: https://github.com/Sanjula2003