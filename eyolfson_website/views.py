from django.shortcuts import render

from blog.models import Post
from publications.models import Publication

def home(request):
    blog_posts = Post.objects.all()
    return render(request, 'home.html', {'blog_posts': blog_posts})

def software(request):
    return render(request, 'software.html')

def cv(request):
    context = {}
    try:
        p = Publication.objects.get(slug='masc-eyolfson')
        context['masc'] = p
    except Publication.DoesNotExist:
        pass
    context['publications'] = Publication.objects.exclude(slug='masc-eyolfson').order_by('-pub_date')
    return render(request, 'cv.html', context)
