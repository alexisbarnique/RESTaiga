# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

import requests

# Página de inicio
def index_view(request):
    template = 'index.html'
    return render(request, template, locals())

def login_view(request):
    user = {}
    if 'username' and 'password' in request.POST:
        username = request.POST['username']
        password = request.POST['password']
        auth = {
            "password": username,
            "type": "normal",
            "username": password
        }
        api = 'http://projects.id.produccion.gob.ar/api/v1/auth' % auth
        response = requests.post(api)
        user = response.json()
        print(user)

    return render(request, 'login.html', {'user': user})

def projects_view(request):
    project = {}
    api = 'http://projects.id.produccion.gob.ar/api/v1/projects'
    response = requests.get(api)
    project = response.json()
    b = 0
    for key in project:
        b = b + 1

    return render(request, 'projects.html', {'project': project, 'b': b})

def users_view(request):
    users = {}
    api = 'http://projects.id.produccion.gob.ar/api/v1/users'
    response = requests.get(api)
    users = response.json()
    a = 0
    for key in users:
        a = a + 1
        print(key)
        print(a)

    return render(request, 'users.html', {'users': users, 'a': a})