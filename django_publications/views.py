from django.shortcuts import get_object_or_404, render

from django_publications.models import Publication

def bibtex(request, slug):
    publication = get_object_or_404(Publication, slug=slug)
    return render(request, 'publications/bibtex.html',
                  {'publication': publication})
