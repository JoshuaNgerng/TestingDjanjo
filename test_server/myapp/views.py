from django.shortcuts import render, HttpResponse
from django.http import HttpRequest

# Create your views here.

def home(request: HttpRequest) -> HttpResponse:
    return render(request, 'home.html')

def login_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'login.html')

def signup_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'signup.html')
