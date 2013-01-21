from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from teaching.models import Offering

def home(request):
    return render(request, 'teaching/home.html',
                  {'offering': Offering.objects.get(id=1)})
