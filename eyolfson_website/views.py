from django.shortcuts import render

from publications.models import Publication

def home(request):
    return render(request, 'home.html')

def cv(request):
    context = {}
    try:
        p = Publication.objects.get(slug='masc-eyolfson')
        context['masc'] = p
    except Publication.DoesNotExist:
        pass
    context['publications'] = Publication.objects.exclude(slug='masc-eyolfson').order_by('-pub_date')
    return render(request, 'cv.html', context)
