# coding: utf-8
from settingsapp.forms.pessoa import FormPessoa
from settingsapp.models.pessoa import PessoaModel
from django.shortcuts import render, redirect
from django.views.generic.base import View


class ConsultaPessoaView(View):
    template = 'index.html'

    def get(self, request):
        pessoas = PessoaModel.objects.all()

        return render(request, self.template, {'pessoas': pessoas})

        # def post(self, request):
        #     return render(request, self.template, {'form': ""})


class CadastroPessoaView(View):
    template = 'pessoa/salvar.html'

    def get(self, request, id=None):

        if id:
            pessoa = PessoaModel.objects.get(pk=id)
            form = FormPessoa(instance=pessoa)
        else:
            form = FormPessoa()

        return render(request, self.template, {'form': form})

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
