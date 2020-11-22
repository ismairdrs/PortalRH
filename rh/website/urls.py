from django.urls import path, include
from .views import HomePageView, save_resumo, home_positions, \
                resumo_register, register_position, position_detail,find_position, save_position


urlpatterns = [
    path('', home_positions, name='home_positions'),
    path('resumo_register/', resumo_register, name='resumo_register'),
    path('register_position/', register_position, name='register_position'),
    path('position/<int:id>/', position_detail, name='position_detail'),
    path('save_resumo/', save_resumo, name='save_resumo'),
    path('find_position', find_position, name='find_position'),
    path('save_position/', save_position, name='save_position'),

]
