# -*- coding: utf-8 -*-
from django.conf.urls import url
from RESTaiga.apps.leafApi.views import *


urlpatterns = [
    url(r'^$', index_view, name='vista_index'),
    url(r'^projects$', projects_view, name='vista_projects'),
    url(r'^users$', users_view, name='vista_users'),
]