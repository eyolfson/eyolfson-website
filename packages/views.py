from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def home(request):
    return render(request, 'packages/home.html')
