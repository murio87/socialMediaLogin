from django.shortcuts import render


def home(request):
    return render(request, 'google_login/home.html')
