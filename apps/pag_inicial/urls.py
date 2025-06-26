from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('auth/', views.auth_view, name='auth'),
    path('meus_casamentos/', views.meus_casamentos, name='meus_casamentos'),

]
