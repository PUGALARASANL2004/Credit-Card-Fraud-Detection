
import joblib
import pandas as pd
import urllib.parse

# Load model
model = joblib.load('fraud_model.sav')

# Get coefficients
coefficients = model.coef_[0]
feature_names = ['Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10', 
                 'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20', 
                 'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'Amount']

# Construct Fraud Case
fraud_values = {}
for feature, coef in zip(feature_names, coefficients):
    if feature == 'Time':
        fraud_values[feature] = 100000 
    elif feature == 'Amount':
        fraud_values[feature] = 1000 if coef > 0 else 0
    else:
        # Use extreme values (5 or -5) based on coefficient direction to maximize fraud score
        fraud_values[feature] = 5 if coef > 0 else -5

# Verify Prediction
input_vector = [fraud_values[f] for f in feature_names]
prediction = model.predict([input_vector])[0]

if prediction == 1:
    print(f"\nSUCCESS: Generated a FRAUD case.")
    # creating query string
    query_params = "&".join([f"{k}={v}" for k, v in fraud_values.items()])
    print(f"\nCLICK THIS LINK TO TEST FRAUD PREDICTION:\nhttp://127.0.0.1:8000/result/?{query_params}")
else:
    print("Failed to generate fraud case.")
