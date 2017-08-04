# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from painelifcapp.models.pessoa import PessoaModel
from painelifcapp.models.turma import TurmaModel
from painelifcapp.models.curso import CursoModel
from django.contrib.auth.models import Group
from painelifcapp.variaveis.variaveis import *
from django.contrib.auth.hashers import make_password
import csv
#from django.
import hashlib

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
        with open('csv/servidores.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for i,row in enumerate(reader):
                print(row)
                nome = row["nome"].split()
                first_name = nome[0].encode('utf-8').title()
                last_name = " ".join(nome[1:]).encode('utf-8').title()
                # print(row)
                if not PessoaModel.objects.filter(username=row['user']):
                    orientador_colaborador = PessoaModel(first_name=first_name,
                                        last_name=last_name,
                                        # group=Group.objects.get(pk__in=[ALUNO]),
                                        username=row["user"],
                                        password=make_password(row["pass"]),
                                        nome=row["nome"].encode('utf-8').title(),
                                        matricula=row["matricula"],

                                        )
                    print(row["tipo"] == 'TAE')
                    if row["tipo"] == 'TAE':
                        orientador_colaborador.save()

                        g=Group.objects.get(pk__in=[COLABORADOR])
                        g.user_set.add(orientador_colaborador)
                        g.save()
                    else:
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

