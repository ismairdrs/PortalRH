from django.shortcuts import render
from .models import Vagas,  Curriculo
from django.views.generic import TemplateView
from django.contrib.auth.models import User
import requests
import json



class HomePageView(TemplateView):
    template_name = 'index.html'

    
def listar_vagas(request, pesquisa=None):
    lista_vagas = Vagas.objects.all()
    data = {
        'vagas': lista_vagas
    }
    return render(request, 'index.html', data)


def pesquisar_vaga(request):
    campo_pesquisado = request.POST['query']
    pesquisa = Vagas.objects.filter(titulo__icontains=campo_pesquisado, descricao__icontains=campo_pesquisado)
    data = {
        'vagas': pesquisa
    }
    return render(request, 'index.html', data)


def salvar_vaga(request):
    Vagas.objects.create(
        titulo=request.POST['demo-titulo'],
        descricao=request.POST['demo-descricao'],
        localizacao=request.POST['demo-location'],
        salario=request.POST['demo-salario'],
        nome_empresa=request.POST['demo-salario'],
        email_contato=request.POST['demo-email']
    )
    return render(request, 'index.html')


def cadastrar_vaga(request):
    return render(request, 'cadastrar_vagas.html')


def vaga_detalhe(request, id):
    vaga = Vagas.objects.get(id=id)
    find = vaga.titulo.split(sep=' ')[0]
    filme = requests.get(f'http://www.omdbapi.com/?t={find}&apikey=66277ea5').json()    
    return render(request, 'vaga_detalhe.html', {'vaga': vaga, 'filme': filme})


def cadastrar_curriculo(request):
    return render(request, 'cadastrar_curriculo.html')


def save_curriculo(request):
    Curriculo.objects.create(
        nome=request.POST['demo-name'],
        sobrenome=request.POST['demo-surname'],
        email=request.POST['demo-email'],
        telefone=request.POST['demo-phone'],
        github=request.POST['demo-github'],
        linkedin=request.POST['demo-linkedin'],
        #descricao=request.POST['demo-descricao'],
        experiencia =request.POST['demo-experiencia'],
        formacoes =request.POST['demo-formacoes'],
        habilidades = request.POST['demo-habilidades'],
        pessoa= request.user
    )
    return render(request, 'index.html')

