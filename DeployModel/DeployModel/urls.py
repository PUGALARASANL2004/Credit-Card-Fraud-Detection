# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),  # Define URL pattern for the contact page
    path('result/', views.result, name='result'),
    path('upload_csv/', views.upload_csv, name='upload_csv'),
    path('chat/', views.chat_bot, name='chat_bot'),
]
