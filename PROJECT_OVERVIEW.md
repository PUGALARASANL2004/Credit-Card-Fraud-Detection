# Credit Card Fraud Detection System

## 1. Project Overview
This project is a **Web-based Machine Learning Application** designed to detect fraudulent credit card transactions in real-time. It provides a user-friendly interface where details of a transaction (Time, Amount, and anonymized features V1-V28) can be entered to check if the transaction is **Legitimate (Safe)** or **Fraudulent**.

## 2. How It Works (The Workflow)
The application follows a simple 3-step process:

1.  **Input**: The user enters transaction details into the web form on the Home Page. These details include:
    *   **Time**: Seconds elapsed since the first transaction.
    *   **Amount**: The value of the transaction.
    *   **V1 - V28**: 28 mathematical features extracted from the original data (using PCA - Principal Component Analysis) to protect user privacy.

2.  **Processing**:
    *   The **Django Backend** captures this data.
    *   It converts the inputs into a numeric format that the computer understands.
    *   It loads a pre-trained **Logistic Regression Model** (`fraud_model.sav`).

3.  **Prediction**:
    *   The model calculates the probability of fraud based on the input patterns.
    *   If the probability is low (e.g., < 50%), it predicts **Safe**.
    *   If the probability is high (e.g., > 50%), it predicts **Fraud**.
    *   The result is displayed immediately to the user.

## 3. Technology Stack
*   **Backend**: Python, Django (Web Framework).
*   **Machine Learning**: Scikit-Learn (Logistic Regression Algorithm), Joblib (Model Loading).
*   **Frontend**: HTML5, CSS3 (Modern "Glassmorphism" Design).
*   **Data Handling**: Numpy (Numerical operations).

## 4. Key Files Explained
*   **`fraud_model.sav`**: The "Brain" of the project. A file containing the mathematical rules learned from training on thousands of past credit card transactions.
*   **`views.py`**: The "Controller". Python code that connects the web page to the machine learning model. It handles the logic of receiving data and getting the prediction.
*   **`templates/home.html`**: The UI where users enter data.
*   **`templates/result.html`**: The UI that shows the red (Fraud) or green (Safe) alert.

## 5. Why V1-V28?
You might notice features labeled `V1` to `V28` instead of "Location" or "Merchant Name". This is standard in financial datasets to ensure **Privacy**. The original data has been transformed mathematically so that no personal information can be read, but the *patterns* of fraud (like unusual amounts at unusual times) remain intact for the AI to detect.
