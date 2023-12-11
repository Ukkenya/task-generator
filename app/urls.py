from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('Shablon/', views.Shablon, name="Shablon"),
    path('vibor/', views.vibor, name="vibor"),
    path('teor/', views.teor, name='teor')
]