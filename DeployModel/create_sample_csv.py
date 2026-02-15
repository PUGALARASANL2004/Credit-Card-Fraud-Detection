
import pandas as pd
import numpy as np

# Create headers
feature_cols = ['Time'] + [f'V{i}' for i in range(1, 29)] + ['Amount']

# 1. Create Safe Transaction (Normal values)
safe_row = [0] + [0.1] * 28 + [10.50]

# 2. Create Fraud Transaction (From our pattern)
fraud_values = {
    'Time': 100000, 'Amount': 1000,
    'V1': 5, 'V2': -5, 'V3': -5, 'V4': 5, 'V5': 5, 
    'V6': -5, 'V7': -5, 'V8': -5, 'V9': -5, 'V10': -5, 
    'V11': 5, 'V12': -5, 'V13': -5, 'V14': -5, 'V15': -5, 
    'V16': -5, 'V17': -5, 'V18': -5, 'V19': 5, 'V20': 5, 
    'V21': -5, 'V22': 5, 'V23': -5, 'V24': 5, 'V25': -5, 
    'V26': -5, 'V27': 5, 'V28': 5
}
fraud_row = [fraud_values.get(col, 0) for col in feature_cols]

# Create DataFrame
df = pd.DataFrame([safe_row, fraud_row, safe_row], columns=feature_cols)

# Save to CSV
df.to_csv('sample_test_data.csv', index=False)
print("Created sample_test_data.csv with 3 transactions (Safe, Fraud, Safe)")
