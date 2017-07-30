# coding=utf-8
from settingsapp.models.trabalho import TrabalhoModel
from django import forms


class FormTrabalho(forms.ModelForm):


    class Meta:
        model = TrabalhoModel
        #fields = ('codigo_pais', 'codigo_cidade', 'numero', 'dono')
        #exclude = ("status",)

        fields = "__all__"
