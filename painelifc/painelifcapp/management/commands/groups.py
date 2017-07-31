# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group

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

    def _create_grupos(self):
        with open('grupos.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for i,row in enumerate(reader):
                if not Group.objects.filter(name=row['nome']):
                    group = Group(name=row['nome'],id=i+1)
                    group.save()


    def handle(self, *args, **options):
        self._create_grupos()

