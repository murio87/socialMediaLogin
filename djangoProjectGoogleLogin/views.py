from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from google_login.models import AccountPeople
from shop.models import Product


def home(request):
    context = {}
    products = Product.objects.all()
    context['products'] = products
    return render(request, 'index.html', context)

