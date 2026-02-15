
import joblib
import numpy as np
import pandas as pd

# Load the model
try:
    model = joblib.load('fraud_model.sav')
    print(f"Model loaded successfully: {type(model)}")
    
    # Check if the model has coefficients (linear models like Logistic Regression do)
    if hasattr(model, 'coef_'):
        coefficients = model.coef_[0]
        intercept = model.intercept_[0]
        
        feature_names = ['Time'] + [f'V{i}' for i in range(1, 29)] + ['Amount']
        
        print("\n--- Model Coefficients (Impact on Fraud Prediction) ---")
        coef_df = pd.DataFrame({'Feature': feature_names, 'Coefficient': coefficients})
        coef_df['Abs_Coefficient'] = coef_df['Coefficient'].abs()
        coef_df = coef_df.sort_values(by='Abs_Coefficient', ascending=False)
        
        print(coef_df.head(10)) # Print top 10 most influential features
        
        # Construct a synthetic "Fraud" transaction
        # To maximize fraud probability (class 1), we want the dot product (inputs * weights) + intercept to be high.
        # If weight is positive, use a high value. If weight is negative, use a low value.
        
        synthetic_fraud_input = []
        print("\n--- Constructing Synthetic Fraud Case ---")
        for feature, coef in zip(feature_names, coefficients):
            if feature == 'Time':
                val = 100000.0 # Arbitrary time
            elif feature == 'Amount':
                val = 0.0 if coef < 0 else 1000.0 # Adjust amount based on sign
            else:
                # For V features (standardized PCA components), values typically range -5 to 5.
                # Let's use fairly extreme values to trigger the class.
                val = 5.0 if coef > 0 else -5.0
            
            synthetic_fraud_input.append(val)
            # print(f"{feature}: {val} (Coef: {coef:.4f})")
            
        # Predict
        prediction = model.predict([synthetic_fraud_input])
        probability = model.predict_proba([synthetic_fraud_input])
        
        print(f"\nSynthetic Input Prediction: {prediction[0]}")
        print(f"Prediction Probability (Safe vs Fraud): {probability[0]}")
        
        if prediction[0] == 1:
            print("\nSUCCESS: Found a fraud case!")
            print("To trigger a fraud alert, try values similar to this synthetic case:")
            for name, val in zip(feature_names, synthetic_fraud_input):
                print(f"{name}={val}")
        else:
            print("\nFAILED: Even mostly extreme values didn't trigger fraud. The intercept might be very low.")
            print(f"Intercept: {intercept}")

    else:
        print("Model does not have coefficients (not a linear model). Cannot explain simply.")

except Exception as e:
    print(f"Error: {e}")
