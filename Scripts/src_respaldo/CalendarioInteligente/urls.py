"""CalendarioInteligente URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth import login

#Hola, cambie las views del calendario
from pages.views import home_view, inicio_view, cuenta_view, calendar_view, config_view, perfil_view, ramos_view
from pag_calendario.views import calendario_view, formularioEventos_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view),
    #path('', inicio_view),
    path('cuenta/', cuenta_view),
    path('calendario/', calendario_view),
    path('perfil/', perfil_view),
    path('config/', config_view),
    path('ramos/', ramos_view),
    path('eventos/', formularioEventos_view),
    path('',LoginView.as_view(template_name='iniciar_sesion.html'), name="login"),
    #path('', login , {'template_name':'iniciar_sesion.html'}, name="login"),
]
