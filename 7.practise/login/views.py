
from django.shortcuts import render

def signup(request):
	context = { 'name':'ABC Farms' }
	return render(request, 'signup.html', context)

