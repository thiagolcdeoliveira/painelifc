"""agenda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# coding=utf-8
from __future__ import unicode_literals

# from appagenda.views import *
from painelifcapp.views.pessoa import ConsultaPessoaView, CadastroPessoaView
from painelifcapp.views.trabalho import ConsultaTrabalhoView, CadastroTrabalhoView, AceitaTrabalhoView, NegaTrabalhoView, ImprimeTrabalhoView
from django.conf.urls import include, url

urlpatterns = [
    url(r'^cadastro-pessoa/$', CadastroPessoaView.as_view(), name='cad-pessoa'),
    url(r'^cadastro-pessoa/(?P<id>\d+)/$', CadastroPessoaView.as_view(), name='edit-pessoa'),
    url(r'^cadastro-trabalho/$', CadastroTrabalhoView.as_view(), name='cad-trabalho'),
    url(r'^cadastro-trabalho/(?P<id>\d+)/$', CadastroTrabalhoView.as_view(), name='edit-trabalho'),
    url(r'^consulta-trabalho/$', ConsultaTrabalhoView.as_view(), name='consu-trabalho'),
    url(r'^consulta-trabalho/(?P<id>\d+)/$', ConsultaTrabalhoView.as_view(), name='trabalho'),
    url(r'^aceita-trabalho/(?P<id>\d+)/(?P<status>\d+)$', AceitaTrabalhoView.as_view(), name='aceita-trabalho'),
    url(r'^nega-trabalho/(?P<id>\d+)/(?P<status>\d+)$', NegaTrabalhoView.as_view(), name='nega-trabalho'),
    url(r'^imprime-trabalho/(?P<id>\d+)/$', ImprimeTrabalhoView.as_view(), name='impri-trabalho'),
]
