# coding: utf-8
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.base import View

from painelifcapp.models.pessoa import PessoaModel
from painelifcapp.models.trabalho import TrabalhoModel
from django.db.models import Q

from painelifcapp.variaveis.variaveis import *


class Home(View):
    template = 'index.html'

    def get(self, request):
        if request.user.is_authenticated:
            trabalhos = TrabalhoModel.objects.filter(
                Q(autor1__pk=request.user.id) | Q(autor2__pk=request.user.id) | Q(autor3__pk=request.user.id) | Q(
                    autor4__pk=request.user.id) | Q(autor5__pk=request.user.id) | Q(autor6__pk=request.user.id) | Q(
                    autor7__pk=request.user.id) | Q(orientador__pk=request.user.id) | Q(
                    colaborador__pk=request.user.id) | Q(usuario=request.user.id)).distinct().count()
            possui_trabalhos = True if trabalhos > 0 else False
            grupo = request.user.groups.filter(pk__in=[ALUNO])[0].pk
            return render(request, self.template, {'possui_trabalhos': possui_trabalhos, 'grupo': grupo})
        else:
            return HttpResponseRedirect(reverse('login'))


class HomeAdminAguardandoListView(ListView):
    model = TrabalhoModel
    queryset = TrabalhoModel.objects.filter(id=AGUARDANDO_PROFESSOR)
    template_name = 'admin/consulta.html'
    context_object_name = 'trabalho'


class HomeAdminSubmetidoListView(ListView):
    model = TrabalhoModel
    queryset = TrabalhoModel.objects.filter(id=SUBMETIDO)
    template_name = 'admin/consulta.html'
    context_object_name = 'trabalho'


class HomeAdminNegadoProfessorListView(ListView):
    model = TrabalhoModel
    queryset = TrabalhoModel.objects.filter(id=NEGADO_PROFESSOR)
    template_name = 'admin/consulta.html'
    context_object_name = 'trabalho'


class HomeAdminListView(ListView):
    model = TrabalhoModel
    queryset = TrabalhoModel.objects.all()
    template_name = 'admin/consulta.html'
    context_object_name = 'trabalho'
