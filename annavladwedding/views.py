from django import forms
from django.shortcuts import redirect, render

class RSVPForm(forms.Form):
    confirmation_code = forms.CharField(max_length=4, widget=forms.TextInput(
        attrs={'class': 'input-mini'}))

def home(request):
    if request.method == 'POST':
        form = RSVPForm(request.POST)
        if form.is_valid():
            return redirect('annavladwedding.views.home')
    else:
        form = RSVPForm()
    return render(request, 'annavladwedding/home.html', {'form': form})
