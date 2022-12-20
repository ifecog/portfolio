from django.shortcuts import render
from .models import About, Skill, Resume

# Create your views here.


def home(request):
    abouts = About.objects.all()
    skills = Skill.objects.all()
    resumes = Resume.objects.all()
    context = {
        'abouts': abouts,
        'skills': skills,
        'resumes': resumes,
    }

    return render(request, 'pages/home.html', context)
