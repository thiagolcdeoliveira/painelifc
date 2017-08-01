# coding=utf-8
from django import forms
from painelifcapp.models.trabalho import TrabalhoModel
from painelifcapp.models.pessoa import PessoaModel
from painelifcapp.forms.validador.colaborador import *
from painelifcapp.forms.validador.orientador import *
from painelifcapp.forms.validador.autor import *
from painelifcapp.variaveis.variaveis import *
from painelifcapp.models.configuracao_trabalho import ConfiguracaoTrabalhoModel

class FormTrabalho(forms.ModelForm):
    class Meta:
        model = TrabalhoModel
        exclude = ("status","usuario")

        # fields = "__all__"


    def __init__(self, *args, **kwargs):
        #id = kwargs.pop('id_turma')

        super(FormTrabalho, self).__init__(*args, **kwargs)
        self.fields['colaborador'].widget = forms.SelectMultiple(attrs={'checked': True},
                    choices=PessoaModel.objects.filter(pk__in=self.colaboradores()).values_list('id', 'username'))

        self.fields['orientador'].widget = forms.Select(attrs={'checked': True},
                    choices=PessoaModel.objects.filter(pk__in=self.orientadores()).values_list('id','username'))

        #self.fields['autor'].widget = forms.CheckboxSelectMultiple(attrs={'checked': False},
        self.fields['autor'].widget = forms.CheckboxSelectMultiple(attrs={'checked': False},
                    choices=PessoaModel.objects.filter(pk__in=self.autores()).values_list('id','username'))

        self.fields['resumo'].widget = forms.Textarea()

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
        if configuracao:
            for colaborador in colaboradores:
                trabalhos = TrabalhoModel.objects.filter(colaborador=colaborador,status__in=[AGUARDANDO_PROFESSOR,SUBMETIDO,APROVADO])

                if (len(trabalhos) <= configuracao.trabalhos_por_colaborador):
                    colaboradores_habilitados.append(colaborador.pk)
        return colaboradores_habilitados

    def orientadores(self):
        orientadores_habilitados=[]
        configuracao=ConfiguracaoTrabalhoModel.objects.order_by("id").last()
        orientadores = PessoaModel.objects.filter(groups__pk__contains=ORIENTADOR)
        if configuracao:
            for orientador in orientadores:
                trabalhos = TrabalhoModel.objects.filter(orientador=orientador,status__in=[AGUARDANDO_PROFESSOR,SUBMETIDO,APROVADO])
                print(len(trabalhos),configuracao.trabalhos_por_orientador)
                if (len(trabalhos) <= configuracao.trabalhos_por_orientador):
                    orientadores_habilitados.append(orientador.pk)
        return orientadores_habilitados

    def autores(self):
        autores_habilitados = []
        configuracao = ConfiguracaoTrabalhoModel.objects.order_by("id").last()
        autores = PessoaModel.objects.filter(groups__pk__contains=ALUNO)
        if configuracao:
            for autor in autores:
                trabalhos = TrabalhoModel.objects.filter(autor=autor,status__in=[AGUARDANDO_PROFESSOR,SUBMETIDO,APROVADO])
                print(len(trabalhos), configuracao.trabalhos_por_autor)
                if (len(trabalhos) < configuracao.trabalhos_por_autor):
                    autores_habilitados.append(autor.pk)
        print(autores_habilitados)
        return autores_habilitados
