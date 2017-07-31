# coding=utf-8
from settingsapp.models.trabalho import TrabalhoModel
from settingsapp.models.pessoa import PessoaModel
from django import forms
from validador.colaborador import  *
from validador.orientador import  *
from validador.autor import  *
from settingsapp.variaveis.variaveis import *
from settingsapp.models.configuracao_trabalho import ConfiguracaoTrabalhoModel

class FormTrabalho(forms.ModelForm):
    class Meta:
        model = TrabalhoModel
        # fields = ('codigo_pais', 'codigo_cidade', 'numero', 'dono')
        # exclude = ("status",)

        fields = "__all__"


    def __init__(self, *args, **kwargs):
    #def __init__(self):
        #id = kwargs.pop('id_turma')
        #turma = Turma.objects.get(id=id)
        #print(PessoaModel.objects.filter(groups__pk__contains=COLABORADOR))

        super(FormTrabalho, self).__init__(*args, **kwargs)
        self.fields['colaborador'].widget = forms.SelectMultiple(attrs={'checked': True},
                                                                 #choices=PessoaModel.objects.filter(groups__pk__contains=COLABORADOR).values_list('id','username'))
                    choices=PessoaModel.objects.filter(pk__in=self.colaboradores()).values_list('id', 'username'))

        self.fields['orientador'].widget = forms.Select(attrs={'checked': True},
                    #choices=PessoaModel.objects.filter(groups__pk__contains=ORIENTADOR).values_list('id','username'))
                    choices=PessoaModel.objects.filter(pk__in=self.orientadores()).values_list('id','username'))

        self.fields['autor'].widget = forms.SelectMultiple(attrs={'checked': True},
                    #choices=PessoaModel.objects.filter(groups__pk__contains=ALUNO).values_list('id','username'))
                    choices=PessoaModel.objects.filter(pk__in=self.autores()).values_list('id','username'))

    def clean_colaborador(self):
        return ValidarColaborador(self.cleaned_data.get('colaborador'))

    def clean_autor(self):
        return ValidarAutor(self.cleaned_data.get('autor'))

    def clean_orientador(self):
        return ValidarOrientador(self.cleaned_data.get('orientador'))

    def colaboradores(self):
        colaboradores_habilitados=[]
        configuracao=ConfiguracaoTrabalhoModel.objects.order_by("id").last()
        colaboradores = PessoaModel.objects.filter(groups__pk__contains=COLABORADOR)
        for colaborador in colaboradores:
            trabalhos = TrabalhoModel.objects.filter(colaborador=colaborador)

            if (len(trabalhos) <= configuracao.trabalhos_por_colaborador):
                colaboradores_habilitados.append(colaborador.pk)
        #print (colaboradores_habilitados)
        return colaboradores_habilitados

    def orientadores(self):
        orientadores_habilitados=[]
        configuracao=ConfiguracaoTrabalhoModel.objects.order_by("id").last()
        orientadores = PessoaModel.objects.filter(groups__pk__contains=ORIENTADOR)
        for orientador in orientadores:
            trabalhos = TrabalhoModel.objects.filter(orientador=orientador)
            print(len(trabalhos),configuracao.trabalhos_por_orientador)
            if (len(trabalhos) <= configuracao.trabalhos_por_orientador):
                orientadores_habilitados.append(orientador.pk)
        #print (orientadores_habilitados)
        return orientadores_habilitados

    def autores(self):
        autores_habilitados = []
        configuracao = ConfiguracaoTrabalhoModel.objects.order_by("id").last()
        autores = PessoaModel.objects.filter(groups__pk__contains=ALUNO)
        for autor in autores:
            trabalhos = TrabalhoModel.objects.filter(autor=autor)
            print(len(trabalhos), configuracao.trabalhos_por_autor)
            if (len(trabalhos) <= configuracao.trabalhos_por_autor):
                autores_habilitados.append(autor.pk)
        # print (autores_habilitados)
        return autores_habilitados
