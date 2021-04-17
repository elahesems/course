from django.shortcuts import render

# Create your views here.
from ui.models import Home


def home (request) :
    home = Home.objects.all()
    context = {'home':home}
    return render(request, 'index.html', context)