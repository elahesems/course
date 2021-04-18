from django.shortcuts import render

# Create your views here.
from ui.models import Home, SocialLinks


def home(request):
    home = Home.objects.all()
    socialLinks = SocialLinks.objects.all()
    context = {'home':home, 'socialLinks':socialLinks}
    return render(request, 'index.html', context)