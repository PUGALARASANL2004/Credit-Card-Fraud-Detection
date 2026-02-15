
from django.shortcuts import render
from django.http import JsonResponse
import joblib
import pandas as pd
import numpy as np
from .chatbot_logic import bot as fraud_bot

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, "home.html")

def result(request):
    # Load your classifier model
    cls = joblib.load('fraud_model.sav')

    # Extract features from the request.GET dictionary
    lis = [
        request.GET['Time'],
        request.GET['V1'],
        request.GET['V2'],
        request.GET['V3'],
        request.GET['V4'],
        request.GET['V5'],
        request.GET['V6'],
        request.GET['V7'],
        request.GET['V8'],
        request.GET['V9'],
        request.GET['V10'],
        request.GET['V11'],
        request.GET['V12'],
        request.GET['V13'],
        request.GET['V14'],
        request.GET['V15'],
        request.GET['V16'],
        request.GET['V17'],
        request.GET['V18'],
        request.GET['V19'],
        request.GET['V20'],
        request.GET['V21'],
        request.GET['V22'],
        request.GET['V23'],
        request.GET['V24'],
        request.GET['V25'],
        request.GET['V26'],
        request.GET['V27'],
        request.GET['V28'],
        request.GET['Amount']
    ]

    # Convert the feature values to numeric type
    lis_numeric = [float(value) for value in lis]

    # Perform prediction using the classifier
    ans = cls.predict([lis_numeric])
    proba = cls.predict_proba([lis_numeric])[0][1] # Probability of class 1 (Fraud)

    # Pass the prediction result to the result.html template
    return render(request, "result.html", {'ans': ans, 'proba': proba})

def upload_csv(request):
    if request.method == 'POST' and request.FILES['file']:
        try:
            # Read CSV File
            csv_file = request.FILES['file']
            df = pd.read_csv(csv_file)
            
            # Ensure columns are in correct order for model (Time, V1..V28, Amount)
            feature_cols = ['Time'] + [f'V{i}' for i in range(1, 29)] + ['Amount']
            
            # Check if all columns exist
            if not all(col in df.columns for col in feature_cols):
                return render(request, "upload.html", {'error': 'CSV must contain Time, V1-V28, and Amount columns.'})
            
            # Select and reorder columns
            model_input = df[feature_cols]
            
            # Load Model
            cls = joblib.load('fraud_model.sav')
            
            # Predict
            predictions = cls.predict(model_input)
            probabilities = cls.predict_proba(model_input)[:, 1] # Get fraud probability
            
            # Add results to DataFrame for display
            df['Prediction'] = predictions
            df['Probability'] = probabilities * 100 # Convert to percentage
            
            # Convert to list of dicts for template
            results = df.to_dict(orient='records')
            
            return render(request, "upload_result.html", {'results': results, 'total_rows': len(results)})
            
        except Exception as e:
            return render(request, "upload.html", {'error': str(e)})
            
    return render(request, "upload.html")

def chat_bot(request):
    msg = request.GET.get('message', '').lower()
    response = fraud_bot.get_response(msg)
    return JsonResponse({'response': response})
