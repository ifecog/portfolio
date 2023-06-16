from django.shortcuts import render, redirect
from .models import About, Skill, Resume, Portfolio, Service

# Create your views here.


def home(request):
    abouts = About.objects.all()
    skills = Skill.objects.all().order_by('upload_time')
    resumes = Resume.objects.all()
    portfolios = Portfolio.objects.all().order_by('-id')
    services = Service.objects.all().order_by('-upload_time')
    context = {
        'abouts': abouts,
        'skills': skills,
        'resumes': resumes,
        'services': services,
        'portfolios': portfolios,
    }

    return render(request, 'pages/home.html', context)


