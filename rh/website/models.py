from django.db import models
from django.contrib.auth.models import User


class Resumo(models.Model):
    name = models.CharField(max_length=30) 
    surname = models.CharField(max_length=250) 
    email = models.EmailField() 
    phone = models.CharField(max_length=11)
    github = models.CharField(max_length=250)
    linkedin = models.CharField(max_length=250)
    description = models.CharField(max_length=2000)
    experience = models.CharField(max_length=2000) 
    formations = models.CharField(max_length=2000) 
    skills = models.CharField(max_length=2000)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')


class Position(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=2500)
    location = models.CharField(max_length=60)
    salary = models.IntegerField()
    name_company = models.CharField(max_length=60, null=True)
    email_contact = models.EmailField()
    
