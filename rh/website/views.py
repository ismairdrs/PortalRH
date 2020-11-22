from django.shortcuts import render
from .models import Position,  Resumo
from django.views.generic import TemplateView
from django.contrib.auth.models import User
import requests
import json



class HomePageView(TemplateView):
    template_name = 'index.html'

    
def home_positions(request):
    list_positions = Position.objects.all()
    data = {
        'list_positions': list_positions
    }
    return render(request, 'index.html', data)


def find_position(request):
    field_find = request.POST['query']
    search = Position.objects.filter(title__icontains=field_find, description__icontains=field_find)
    data = {
        'position': search
    }
    return render(request, 'index.html', data)


def save_position(request):
    Position.objects.create(
        title=request.POST['demo-title'],
        description=request.POST['demo-description'],
        location=request.POST['demo-location'],
        salary=request.POST['demo-salary'],
        name_company=request.POST['demo-name_company'],
        email_contact=request.POST['demo-email_contact']
    )
    return render(request, 'index.html')


def register_position(request):
    return render(request, 'register_position.html')


def position_detail(request, id):
    position = Position.objects.get(id=id)
    find = position.title.split(sep=' ')[0]
    movie = requests.get(f'http://www.omdbapi.com/?t={find}&apikey=66277ea5').json()    
    return render(request, 'position_detail.html', {'position': position, 'movie': movie})


def resumo_register(request):
    return render(request, 'resumo_register.html')


def save_resumo(request):
    Resumo.objects.create(
        name=request.POST['demo-name'],
        surname=request.POST['demo-surname'],
        email=request.POST['demo-email'],
        phone=request.POST['demo-phone'],
        github=request.POST['demo-github'],
        linkedin=request.POST['demo-linkedin'],
        experience =request.POST['demo-experience'],
        formations =request.POST['demo-formations'],
        skills = request.POST['demo-skills'],
        user= request.user
    )
    return render(request, 'index.html')

