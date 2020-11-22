from django.db import models
from django.contrib.auth.models import User


class Curriculo(models.Model):
    nome = models.CharField(max_length=30) 
    sobrenome = models.CharField(max_length=250) 
    email = models.EmailField() # importar o email do cadastro
    telefone = models.CharField(max_length=11)
    github = models.CharField(max_length=250)
    linkedin = models.CharField(max_length=250)
    desricao = models.CharField(max_length=2000)
    experiencia = models.CharField(max_length=2000) 
    formacoes = models.CharField(max_length=2000) 
    habilidades = models.CharField(max_length=2000)
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE, related_name='curriculos')


class Vagas(models.Model):
    titulo = models.CharField(max_length=250)
    descricao = models.CharField(max_length=2500)
    localizacao = models.CharField(max_length=60)
    salario = models.IntegerField()
    nome_empresa = models.CharField(max_length=60, null=True)
    email_contato = models.EmailField()
    
