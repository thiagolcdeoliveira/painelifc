# coding: utf-8

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic.base import View


class Home(View):
    template = 'index.html'

    def get(self, request):


        return render(request, self.template, {})

        # def post(self, request):
        #     return render(request, self.template, {'form': ""})

