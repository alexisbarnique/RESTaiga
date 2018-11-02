# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from taiga import TaigaAPI

import requests

api = TaigaAPI(
    host='http://projects.id.produccion.gob.ar/api/v1/projects',
    tls_verify=False
)

# Página de inicio
def index_view(request):
    template = 'index.html'
    return render(request, template, locals())

def projects_view(request):
    user = {}
    if 'username' in request.GET:
        username = request.GET['username']
        url = 'https://api.github.com/users/%s' % username
        response = requests.get(url)
        user = response.json()

    return render(request, 'users.html', {'user': user})
