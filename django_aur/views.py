from django.shortcuts import render
from django_aur.models import Update

def aur(request):
    return render(request, 'django_aur/aur.html',
                  {'updates': Update.objects.order_by('package', '-time')
                   .distinct('package')})
