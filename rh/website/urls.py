from django.urls import path, include
from .views import HomePageView, save_curriculo, listar_vagas, \
                cadastrar_curriculo, cadastrar_vaga, vaga_detalhe,pesquisar_vaga, salvar_vaga


urlpatterns = [
    path('', listar_vagas, name='home_vagas'),
    path('cadastrar_curriculo/', cadastrar_curriculo, name='cadastrar_curriculo'),
    path('cadastrar_vaga/', cadastrar_vaga, name='cadastrar_vaga'),
    path('vaga/<int:id>/', vaga_detalhe, name='vaga_detalhe'),
    path('save_curriculo/', save_curriculo, name='save_curriculo'),
    path('pesquisar_vaga', pesquisar_vaga, name='pesquisar_vaga'),
    path('salvar_vaga/', salvar_vaga, name='salvar_vaga'),

]
