# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group
from painelifcapp.models.configuracao_trabalho import ConfiguracaoTrabalhoModel
import csv


class Command(BaseCommand):


    def _create_configuracoestrabalho(self):
        with open('csv/configuracoestrabalho.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for i,row in enumerate(reader):
                #print(row)
                configuracaotrabalho = ConfiguracaoTrabalhoModel(name=row['nome'],min_colaborador=row["min_colaborador"],
                                                                 max_colaborador=row["max_colaborador"],min_autor=row["max_autor"],
                                                                 max_autor=row["max_autor"],trabalhos_por_colaborador=row["max_trabalho_colaborador"],
                                                                 trabalho_por_orientador=row["max_trabalho_orientador"],
                                                                 trabalho_por_autor=row["max_trabalho_autor"],min_disciplina=row["min_disciplina"],
                                                                 max_disciplina=row["max_disciplina"])
                configuracaotrabalho.save()


    def handle(self, *args, **options):
        self._create_configuracoestrabalho()

