# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from painelifcapp.models.pessoa import PessoaModel
from painelifcapp.models.turma import TurmaModel
from painelifcapp.models.curso import CursoModel
from django.contrib.auth.models import Group
from painelifcapp.variaveis.variaveis import *
import csv


class Command(BaseCommand):
    args = '<foo bar ...>'
    help = '''Deve conter um csv intitulado "projetos.csv" na raiz do projeto.'
           Deve conter os cabeçalhos:
           "Qual o nome do projeto?",
           "Qual tipo do projeto?",
           "O projeto está em desenvolvimento?",
           "URL  do projeto, se ele estiver  disponível.",
           "Descrição" e
           "Qual o lattes? ".'''


    def _create_orientador_colaborador(self):
        with open('csv/alunos.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            print(Group.objects.filter(pk__in=[ORIENTADOR,COLABORADOR]))
            for i,row in enumerate(reader):
                if not PessoaModel.objects.filter(username=row['usuario']):
                    orientador_colaborador = PessoaModel(first_name=row['nome'],
                     last_name=row["sobrenome"],
                     username=row["usuario"],
                     password=""                    )


                    g=Group.objects.filter(pk__in=[ORIENTADOR,COLABORADOR])
                    orientador_colaborador.save()
                    for i in g:
                        i.user_set.add(orientador_colaborador)
                        i.save()
                        '''orientador_colaborador.save()
                    g=Group.objects.get(pk__in=[ORIENTADOR])
                    g.user_set.add(orientador_colaborador)
                    g.save()
                    g=Group.objects.get(pk__in=[COLABORADOR])
                    g.user_set.add(orientador_colaborador)
                    g.save()'''
                    #aluno.save()



    def handle(self, *args, **options):

        self._create_orientador_colaborador()

