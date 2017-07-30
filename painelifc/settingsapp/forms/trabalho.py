# coding=utf-8
from settingsapp.models.trabalho import TrabalhoModel
from django import forms
from validador.colaborador import  *
from validador.orientador import  *
from validador.autor import  *


class FormTrabalho(forms.ModelForm):


    class Meta:
        model = TrabalhoModel
        #fields = ('codigo_pais', 'codigo_cidade', 'numero', 'dono')
        #exclude = ("status",)

        fields = "__all__"

    def clean_colaborador(self):
        return ValidarColaborador(self.cleaned_data.get('colaborador'))

    def clean_autor(self):
        return ValidarAutor(self.cleaned_data.get('autor'))
    def clean_orientador(self):
        return ValidarOrientador(self.cleaned_data.get('orientador'))
