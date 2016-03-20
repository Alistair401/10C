from django.conf.urls import patterns, include, url
from django.contrib import admin
from mainapp import views

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url('^mainapp/', include('mainapp.urls')),
                       url(r'^$', include('mainapp.urls')),

)
