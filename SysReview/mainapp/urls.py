__author__ = 'uni'

from django.conf.urls import patterns, url
from mainapp import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       )
