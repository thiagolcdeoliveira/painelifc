# coding: utf-8
from painelifcapp.forms.pessoa import FormPessoa
from painelifcapp.models.pessoa import PessoaModel
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class ConsultaPessoaView(View):
    template = 'index.html'

    @method_decorator(login_required)
    def get(self, request):
        pessoas = PessoaModel.objects.all()
        return render(request, self.template, {'pessoas': pessoas})


class CadastroPessoaView(View):
    template = 'pessoa/salvar.html'

    @method_decorator(login_required)
    def get(self, request, id=None):
        if id:
            pessoa = PessoaModel.objects.get(pk=id)
            form = FormPessoa(instance=pessoa)
        else:
            form = FormPessoa()
        return render(request, self.template, {'form': form})

    @method_decorator(login_required)
    def post(self, request, id=None):
        if id:
            pessoa = PessoaModel.objects.get(pk=id)
            form = FormPessoa(instance=pessoa, data=request.POST)
        else:
            form = FormPessoa(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request, self.template, {'form': form})


