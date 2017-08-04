# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from painelifcapp.models.pessoa import PessoaModel
from painelifcapp.models.disciplina import DisciplinaModel
from painelifcapp.models.curso import CursoModel
from django.contrib.auth.models import Group
from painelifcapp.variaveis.variaveis import *
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


    def _create_disciplina(self):
        with open('csv/disciplinas_import.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for i,row in enumerate(reader):

                if not DisciplinaModel.objects.filter(nome=row['disciplina']):
                    disciplina = DisciplinaModel(nome=row['disciplina'],

                                        )


                    disciplina.save()



    def handle(self, *args, **options):

        self._create_disciplina()

