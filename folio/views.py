from django.shortcuts import render, redirect
from .models import About, Skill, Resume, Portfolio, Service
from django.core.mail import send_mail
from portfolio import settings
from django.contrib import messages

# Create your views here.


def home(request):
    abouts = About.objects.all()
    skills = Skill.objects.all().order_by('upload_time')
    resumes = Resume.objects.all()
    portfolios = Portfolio.objects.all()
    services = Service.objects.all().order_by('upload_time')
    context = {
        'abouts': abouts,
        'skills': skills,
        'resumes': resumes,
        'services': services,
        'portfolios': portfolios,
    }

    return render(request, 'pages/home.html', context)


