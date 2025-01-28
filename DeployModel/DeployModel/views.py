# views.py

from django.http import HttpResponse
from django.shortcuts import render
import joblib
# views.py

from django.shortcuts import render
# views.py

from django.shortcuts import render

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

    # Pass the prediction result to the result.html template
    return render(request, "result.html", {'ans': ans})
