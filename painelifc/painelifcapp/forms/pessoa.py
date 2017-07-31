# coding=utf-8
from painelifcapp.models.pessoa import PessoaModel
from django import forms
from validador import  *

class FormPessoa(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Senha')
    username = forms.CharField(label='Nome de Usuário')
    first_name = forms.CharField(label='Primeiro Nome')
    last_name = forms.CharField(label='Sobrenome')
    email = forms.EmailField(label='E-mail')


    def save(self, commit=True):
        user = super(FormPessoa, self).save(commit=True)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()



    class Meta:
        model = PessoaModel
        fields = ('username', 'email', 'first_name', 'last_name', 'password','groups','matricula')
        exclude = ("date_joined", "is_active", "user_permissions", "last_login", "is_staff", "is_superuser")
        # fields = "__all__"
