# coding: utf-8
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.base import View
from painelifcapp.models.trabalho import TrabalhoModel
from django.db.models import Q


class Home(View):
    template = 'index.html'

    def get(self, request):
        if request.user.is_authenticated:
            trabalhos = TrabalhoModel.objects.filter(
                Q(autor__pk=request.user.id) | Q(orientador__pk=request.user.id) | Q(
                    colaborador__pk=request.user.id) | Q(usuario=request.user.id)).distinct().count()
            possui_trabalhos = True if trabalhos > 0 else False
            return render(request, self.template, {'possui_trabalhos': possui_trabalhos})
        else:
            return HttpResponseRedirect(reverse('login'))

