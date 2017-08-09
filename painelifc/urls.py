"""painelifc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from __future__ import unicode_literals

from django.conf.urls import url, include
from django.contrib import admin
from painelifcapp.views.home import Home
from django.contrib.auth.views import login, logout, password_change, password_change_done

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Home.as_view(), name='home'),
    url(r'^(?P<status>\d+)/$', Home.as_view(), name='home-admin'),
    url(r'^login/$', login, {'template_name': 'login/login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'login/logout.html'}, name='logout'),
    url(r'^', include('painelifcapp.urls')),
    url(r'^accounts/password/change/$', password_change, {
        'template_name': 'alterSenha/alterSenhaForm.html'},
        name='password_change'),
    url(r'^accounts/password/change/done/$', password_change_done,
        {'template_name': 'alterSenha/alterSenhaFeito.html'},
        name='password_change_done'),
]
