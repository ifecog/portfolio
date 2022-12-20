from django.shortcuts import render
from .models import About, Skill

# Create your views here.


def home(request):
    abouts = About.objects.all()
    skills = Skill.objects.all()
    context = {
        'abouts': abouts,
        'skills': skills,
    }

    return render(request, 'pages/home.html', context)
