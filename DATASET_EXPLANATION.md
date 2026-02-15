# Why 30 Inputs?

The model requires exactly **30 input fields** because it was trained on a dataset with **30 specific features**. Here is what they represent:

## 1. The Anonymized Features (28 Inputs: V1 - V28)
*   **What are they?** These are numerical values resulting from a mathematical transformation called **PCA (Principal Component Analysis)**.
*   **Why use them?** Real credit card data contains sensitive private information like:
    *   User Name
    *   Credit Card Number
    *   Merchant Name
    *   Location
*   **Privacy Protection:** To protect user privacy, the bank that released this dataset transformed these sensitive details into abstract numbers (`V1`, `V2`, ... `V28`).
    *   Example: `V1` might be a combination of "Location" and "Spending Habit," but we can't reverse it to find the original location.
*   **Model Logic:** Even though *we* don't know what `V14` means, the **Model** learned that when `V14` is very low (e.g., -5), it correlates strongly with fraud.

## 2. Time (1 Input)
*   **What is it?** The number of seconds elapsed between this transaction and the very first transaction in the dataset.
*   **Why is it important?** Fraud often happens at unusual times (e.g., 3:00 AM) or in rapid succession. The model uses this to spot timing patterns.

## 3. Amount (1 Input)
*   **What is it?** The transaction value.
*   **Why is it important?** Fraudsters often test cards with small amounts or try to steal large sums. The amount is a critical indicator.

## Summary
*   **28 "V" Features** (Privacy-protected user data)
*   **+ 1 Time Feature** (When it happened)
*   **+ 1 Amount Feature** (How much money)
*   **= 30 Total Inputs**

**Crucially:** The model is a mathematical equation. It expects a vector of size 30. If you give it 29 or 31 inputs, the math won't work, and the code will crash.
