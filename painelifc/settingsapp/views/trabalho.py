# coding: utf-8
from settingsapp.forms.trabalho import FormTrabalho
from settingsapp.models.trabalho import TrabalhoModel
#from settingsapp.models.pessoa import PessoaModel
from settingsapp.models.pessoa import PessoaModel
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib.auth.models import User
from django.db.models import Q
from settingsapp.variaveis.variaveis import *

class ConsultaTrabalhoView(View):
    template = 'index.html'
    template_consulta='trabalho/consulta.html'

    def get(self, request,id=None):
        if id:
            try:
                autorizacao = TrabalhoModel.objects.filter( Q(colaborador__pk=request.user.id) | Q(orientador__pk=request.user.id)| Q(autor__pk=request.user.id) | Q (usuario=request.user.id)).distinct()
                admin=PessoaModel.objects.get(pk=request.user.id).groups.filter(pk=ADMIN)
                if(autorizacao or admin):
                     trabalho = TrabalhoModel.objects.get(pk=id)
                     return render(request, self.template_consulta, {'trabalho': trabalho})
                else:
                     return redirect('/')
            except:
                return redirect('/')

        else:
            #trabalhos = TrabalhoModel.objects.all()
            trabalhos = TrabalhoModel.objects.filter( Q(autor__pk=request.user.id) | Q (usuario=request.user.id)).distinct()
            pessoa=PessoaModel.objects.filter(pk=request.user.id)
            print(pessoa)
            pessoa=PessoaModel.objects.filter(user_ptr_id=request.user.id)
            print(pessoa)


            return render(request, self.template, {'trabalhos': trabalhos})

        # def post(self, request):
        #     return render(request, self.template, {'form': ""})

class CadastroTrabalhoView(View):
    template = 'trabalho/salvar.html'

    def get(self, request, id=None):

        if id:
            trabalho = TrabalhoModel.objects.get(pk=id)

            form = FormTrabalho(instance=trabalho)
        else:
            form = FormTrabalho()
        return render(request, self.template, {'form': form})

    def post(self, request, id=None):

        if id:
            trabalho = TrabalhoModel.objects.get(pk=id)
            form = FormTrabalho(instance=trabalho, data=request.POST)
        else:

            form = FormTrabalho(request.POST)
        print(request.POST)
        if form.is_valid():
            form_edit = form.save(commit=True)
            '''pessoa=PessoaModel.objects.filter(user_ptr_id=request.user.id)

            #form_edit.usuario_id = request.user.id
            if pessoa:
                form_edit.usuario_id = pessoa[0].id'''
            form_edit.usuario_id = request.user.id
            form_edit.status_id = AGURADANDO_PROFESSOR

            form_edit.save()
            #form.save()
            return redirect('/')

        return render(request, self.template, {'form': form})
