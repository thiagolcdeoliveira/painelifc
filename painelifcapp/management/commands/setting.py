# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group
from painelifcapp.models.setting import SettingModel

import csv


class Command(BaseCommand):


    def _create_setting(self):
        with open('csv/setting.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for i,row in enumerate(reader):
                setting = SettingModel(name=row['name'], endereco=row['endereco'], logo=row['logo'], imagem_titulo=row['imagem_titulo'],
                                       git=row['git'], instagram=row['instagram'], facebook=row['facebook'], site=row['site'])
                setting.save()


    def handle(self, *args, **options):
        self._create_setting()

