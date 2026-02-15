
import joblib
import sklearn

try:
    model = joblib.load('fraud_model.sav')
    print(f"Model Type: {type(model)}")
    print(f"Model Description: {model}")
except Exception as e:
    print(f"Error loading model: {e}")
