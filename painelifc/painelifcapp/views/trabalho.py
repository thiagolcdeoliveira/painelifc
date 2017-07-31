# coding: utf-8
from painelifcapp.forms.trabalho import FormTrabalho
from painelifcapp.models.trabalho import TrabalhoModel
#from painelifcapp.models.pessoa import PessoaModel
from painelifcapp.models.pessoa import PessoaModel
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib.auth.models import User
from django.db.models import Q
from painelifcapp.variaveis.variaveis import *



class ConsultaTrabalhoView(View):
    template = 'index.html'
    template_consulta='trabalho/consulta.html'

    def get(self, request, id=None):
        if id:
            print(request.user.id)
            print('oi')
            try:
                autorizacao = TrabalhoModel.objects.filter(Q(colaborador__pk=request.user.id) | Q(orientador__pk=request.user.id) | Q(autor__pk=request.user.id) | Q (usuario=request.user.id)).distinct()
                admin = request.user.is_superuser or PessoaModel.objects.get(pk=request.user.id).groups.filter(pk=ADMIN)
                print(autorizacao)
                print(admin)
                if(autorizacao or admin):
                     trabalho = TrabalhoModel.objects.get(pk=id)
                     return render(request, self.template_consulta, {'trabalho': trabalho})
                else:
                     return redirect('/')
            except:
                return redirect('/')

        else:
            print('oi2')
            #trabalhos = TrabalhoModel.objects.all()
            trabalhos = TrabalhoModel.objects.filter(Q(autor__pk=request.user.id) | Q(usuario=request.user.id) | Q(orientador__pk=request.user.id) | Q(colaborador__pk=request.user.id)).distinct()
            is_orientador = PessoaModel.objects.filter(pk=request.user.id, groups__in=[ORIENTADOR]).exists()
            print(is_orientador)
            return render(request, self.template, {'trabalhos': trabalhos, 'orientador': is_orientador})

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
            form_edit.usuario_id = request.user.id
            form_edit.status_id = AGUARDANDO_PROFESSOR
            form_edit.save()
            #form.save()
            return redirect('/')

        return render(request, self.template, {'form': form})
