# coding=utf-8
from django import forms
from django.forms import Textarea

from painelifcapp.models.status import StatusModels
from painelifcapp.models.trabalho import TrabalhoModel
from painelifcapp.models.pessoa import PessoaModel
from painelifcapp.forms.validador.colaborador import *
from painelifcapp.forms.validador.orientador import *
from painelifcapp.forms.validador.autor import *
from painelifcapp.forms.validador.disciplina import *
from painelifcapp.forms.validador.resumo import *
from painelifcapp.variaveis.variaveis import *
from painelifcapp.models.configuracao_trabalho import ConfiguracaoTrabalhoModel
from painelifcapp.models.disciplina import DisciplinaModel


class FormTrabalho(forms.ModelForm):

    class Meta:
        model = TrabalhoModel
        # widgets = {"text": Textarea(required=False)}

        # exclude = ("usuario", )

        fields = "__all__"

    def __init__(self, *args, **kwargs):
        #id = kwargs.pop('id_turma')
        status = StatusModels.objects.filter(
            pk=AGUARDANDO_PROFESSOR).values_list('id', 'descricao')
        super(FormTrabalho, self).__init__(*args, **kwargs)
        self.fields['colaborador'].widget = forms.SelectMultiple(attrs={'checked': True, 'class': 'search selection'},
                    choices=PessoaModel.objects.filter(pk__in=self.colaboradores()).values_list('id', 'nome'))

        self.fields['orientador'].widget = forms.Select(attrs={'checked': True, 'class': 'search selection'},
                    choices=PessoaModel.objects.filter(pk__in=self.orientadores()).values_list('id','nome'))
        # self.fields['autor1'].widget = forms.Select(attrs={'checked': True, 'class': 'search selection'},
        #                                                 choices=PessoaModel.objects.filter(
        #                                                     pk__in=self.autores()).values_list('id', 'nome'))
        self.fields['autor2'].widget = forms.Select(attrs={'checked': True, 'class': 'search selection'},
                                                        choices=PessoaModel.objects.filter(pk__in=self.autores()).values_list('id', 'nome'))
        self.fields['autor3'].widget = forms.Select(attrs={'checked': True, 'class': 'search selection'},
                                                        choices=PessoaModel.objects.filter(pk__in=self.autores()).values_list('id', 'nome'))
        self.fields['autor4'].widget = forms.Select(attrs={'checked': True, 'class': 'search selection'},
                                                        choices=PessoaModel.objects.filter(pk__in=self.autores()).values_list('id', 'nome'))
        self.fields['autor5'].widget = forms.Select(attrs={'checked': True, 'class': 'search selection'},
                                                        choices=PessoaModel.objects.filter(pk__in=self.autores()).values_list('id', 'nome'))
        self.fields['autor6'].widget = forms.Select(attrs={'checked': True, 'class': 'search selection'},
                                                        choices=PessoaModel.objects.filter(pk__in=self.autores()).values_list('id', 'nome'))
        self.fields['autor7'].widget = forms.Select(attrs={'checked': True, 'class': 'search selection'},
                                                        choices=PessoaModel.objects.filter(pk=0).values_list('id', 'nome'))

        # self.fields['autor1'].widget.attrs['readonly'] = True
        self.fields['autor1'].required = False
        self.fields['autor2'].required = False
        self.fields['autor3'].required = False
        self.fields['autor4'].required = False
        self.fields['autor5'].required = False
        self.fields['autor6'].required = False
        self.fields['autor7'].required = False
        self.fields['orientador'].required = False
        self.fields['colaborador'].required = False
        self.fields['disciplina'].required = False
        self.fields['resumo'].required = False
        self.fields['titulo'].required = False

        #self.fields['autor'].widget = forms.CheckboxSelectMultiple(attrs={'checked': False},
        # self.fields['autor1'].widget = forms.Select(attrs={'required':False,'checked': False, 'placeholder': 'Selecione uma turma primeiro', 'class': 'search selection'})
        # self.fields['autor2'].widget = forms.Select(attrs={'checked': False, 'class': 'search selection'})
        # self.fields['autor3'].widget = forms.Select(attrs={'checked': False, 'class': 'search selection'})
        # self.fields['autor4'].widget = forms.Select(attrs={'checked': False, 'class': 'search selection'})
        # self.fields['autor5'].widget = forms.Select(attrs={'checked': False, 'class': 'search selection'})
        # self.fields['autor6'].widget = forms.Select(attrs={'checked': False, 'class': 'search selection'})
        # self.fields['autor7'].widget = forms.Select(attrs={'checked': False, 'class': 'search selection'})

        self.fields['disciplina'].widget = forms.SelectMultiple(attrs={'checked': False, 'placeholder': 'Selecione uma turma primeiro', 'class': 'search selection'},
                                                                choices=DisciplinaModel.objects.all().values_list('id',
                                                                                                            'nome')
                                                                )

        self.fields['status'].widget = forms.HiddenInput(attrs={'value': status[0][0]})

        self.fields['resumo'].widget = forms.Textarea()

    def clean_colaborador(self):
        return ValidarColaborador(self.cleaned_data.get('colaborador'))

    # def clean(self):
    #     print("ooooo")
    #     return ValidarAutor(self)

    def clean_orientador(self):
        return ValidarOrientador(self.cleaned_data.get('orientador'))

    def clean_resumo(self):
        return ValidarResumo(self.cleaned_data.get('resumo'))

    def clean_disciplina(self):
        return ValidarDisciplina(self.cleaned_data.get('disciplina'))

    def colaboradores(self):
        colaboradores_habilitados=[]
        configuracao=ConfiguracaoTrabalhoModel.objects.order_by("id").last()
        colaboradores = PessoaModel.objects.filter(groups__pk__contains=COLABORADOR)
        if configuracao:
            for colaborador in colaboradores:
                trabalhos = TrabalhoModel.objects.filter(colaborador=colaborador,status__in=[SUBMETIDO,APROVADO])

                if (len(trabalhos) < configuracao.trabalhos_por_colaborador):
                    colaboradores_habilitados.append(colaborador.pk)
        return colaboradores_habilitados

    def orientadores(self):
        orientadores_habilitados=[]
        configuracao=ConfiguracaoTrabalhoModel.objects.order_by("id").last()
        orientadores = PessoaModel.objects.filter(groups__pk__contains=ORIENTADOR)
        if configuracao:
            for orientador in orientadores:
                trabalhos = TrabalhoModel.objects.filter(orientador=orientador,status__in=[SUBMETIDO,APROVADO])
                if (len(trabalhos) < configuracao.trabalhos_por_orientador):
                    orientadores_habilitados.append(orientador.pk)
        return orientadores_habilitados

    def autores(self):
        # autores_habilitados = []
        # configuracao = ConfiguracaoTrabalhoModel.objects.order_by("id").last()
        # autores = PessoaModel.objects.filter(groups__pk__contains=ALUNO)
        # if configuracao:
        #     for autor in autores:
        #         trabalhos = TrabalhoModel.objects.filter(autor=autor,status__in=[SUBMETIDO,APROVADO])
        #         print(len(trabalhos), configuracao.trabalhos_por_autor)
        #         if (len(trabalhos) < configuracao.trabalhos_por_autor):
        #             autores_habilitados.append(autor.pk)
        # print(autores_habilitados)

        # return autores_habilitados
        return PessoaModel.objects.filter(groups__pk__contains=ALUNO)