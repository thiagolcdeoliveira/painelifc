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

    def _create_curso(self):
        with open('csv/alunos.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row)
                if not CursoModel.objects.filter(nome=row['curso']):
                    curso = CursoModel(nome=row['curso'])
                    curso.save()

    def _create_turma(self):
        with open('csv/alunos.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row)
                if not TurmaModel.objects.filter(nome=row['turma']):
                    turma =TurmaModel(nome=row['turma'],
                    curso=CursoModel.objects.get(nome=row["curso"])
                                      )
                    turma.save()

    def _create_aluno(self):
        with open('csv/alunos.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for i,row in enumerate(reader):
                if not PessoaModel.objects.filter(username=row['usuario']):
                    aluno = PessoaModel(first_name=row['nome'],
                     turma=TurmaModel.objects.get(nome=row['turma']),
                     last_name=row["sobrenome"],
                    #group=Group.objects.filter(pk__in=[ALUNO])
                     username=row["usuario"]
                                         )
                    aluno.save()



    def handle(self, *args, **options):
        self._create_curso()
        self._create_turma()
        self._create_aluno()
