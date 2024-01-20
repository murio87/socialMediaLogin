from django.shortcuts import render
from google_login.models import AccountPeople


def home(request):
	context = {}
	users = AccountPeople.objects.all()
	context['users'] = users
	return render(request, 'index.html', context)